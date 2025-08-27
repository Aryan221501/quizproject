import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import redirect_to_login
from django.http import JsonResponse, HttpResponseBadRequest
from django.db import models, transaction
from django.db.models import Count, Avg, Sum
from django.utils import timezone
from django.core.cache import cache
from django.core.paginator import Paginator
from .models import Quiz, Question, QuizAttempt, Category
from .forms import UserRegistrationForm

# Set up logging
logger = logging.getLogger(__name__)

def home(request):
    # Use caching for homepage data
    cache_key = 'homepage_data'
    cached_data = cache.get(cache_key)
    
    if cached_data is None:
        categories = Category.objects.prefetch_related('quizzes').annotate(
            quiz_count=Count('quizzes')
        ).all()
        
        latest_attempts = QuizAttempt.objects.select_related(
            'quiz', 'user'
        ).order_by('-completed_at')[:5] if request.user.is_authenticated else []
        
        cached_data = {
            'categories': categories,
            'latest_attempts': latest_attempts,
        }
        # Cache for 5 minutes
        cache.set(cache_key, cached_data, 300)
    
    return render(request, 'quiz/home.html', cached_data)

def quiz_list(request):
    quizzes = Quiz.objects.select_related('category').filter(is_active=True)
    
    # Add pagination
    paginator = Paginator(quizzes, 12)  # Show 12 quizzes per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'quiz/quiz_list.html', {'page_obj': page_obj})

def quiz_detail(request, quiz_id):
    # Redirect to login if user is not authenticated
    if not request.user.is_authenticated:
        return redirect_to_login(request.get_full_path(), '/login/', 'next')
    
    # Use select_related and prefetch_related to avoid N+1 queries
    quiz = get_object_or_404(
        Quiz.objects.prefetch_related(
            'questions__options'
        ).select_related('category'), 
        id=quiz_id, 
        is_active=True
    )
    
    return render(request, 'quiz/quiz_detail.html', {'quiz': quiz})

@login_required
def quiz_history(request):
    # Optimize query with proper select_related
    attempts = QuizAttempt.objects.filter(user=request.user).select_related(
        'quiz', 'quiz__category'
    ).order_by('-completed_at')
    
    paginator = Paginator(attempts, 10)  # Show 10 attempts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'quiz/quiz_history.html', {'page_obj': page_obj})

def leaderboard(request):
    # Optimize leaderboard query
    top_users = QuizAttempt.objects.select_related('user').values(
        'user__username'
    ).annotate(
        avg_score=Avg('percentage'),
        total_quizzes=Count('quiz'),
        total_points=Sum('score')
    ).filter(
        total_quizzes__gte=3  # Only users with at least 3 quizzes
    ).order_by('-avg_score')[:10]
    
    return render(request, 'quiz/leaderboard.html', {'top_users': top_users})

@login_required
def profile(request):
    user = request.user
    
    # Optimize profile queries
    attempts = QuizAttempt.objects.filter(user=user).select_related('quiz')
    
    # Calculate statistics efficiently
    stats = attempts.aggregate(
        total_quizzes=Count('id'),
        avg_score=Avg('percentage'),
        best_score=Avg('percentage'),
        total_points=Sum('score')
    )
    
    context = {
        'user': user,
        'total_quizzes': stats['total_quizzes'] or 0,
        'avg_score': stats['avg_score'] or 0,
        'best_score': stats['best_score'] or 0,
        'total_points': stats['total_points'] or 0,
        'attempts': attempts[:5],  # Only recent attempts
    }
    return render(request, 'quiz/profile.html', context)

def quiz_view(request):
    # Redirect to login if user is not authenticated
    if not request.user.is_authenticated:
        return redirect_to_login(request.get_full_path(), '/login/', 'next')
    
    # Get the first active quiz
    quiz = Quiz.objects.prefetch_related(
        "questions__options"
    ).select_related("category").filter(is_active=True).first()
    
    if not quiz:
        return render(request, "quiz/no_quiz.html")
        
    return render(request, "quiz/quiz.html", {"quiz": quiz})

@login_required
@transaction.atomic  # Ensure data consistency
def submit(request):
    if request.method != "POST":
        return redirect("quiz")
    
    try:
        quiz_id = request.POST.get("quiz_id")
        if not quiz_id:
            return HttpResponseBadRequest("Quiz ID is required")
            
        quiz = get_object_or_404(Quiz, id=quiz_id, is_active=True)
        
        # Calculate maximum possible score
        max_score = quiz.questions.aggregate(
            total_points=Sum('points')
        )['total_points'] or 0
        
        score = 0
        total_points = 0
        
        # Process each question efficiently
        for question in quiz.questions.all():
            total_points += question.points
            selected = request.POST.get(str(question.id))
            
            if selected:
                try:
                    selected_option = question.options.get(id=int(selected))
                    if selected_option.is_correct:
                        score += question.points
                except (ValueError, question.options.model.DoesNotExist):
                    # Invalid selection, skip it
                    logger.warning(f"Invalid option selection for question {question.id}")
                    pass
        
        # Save the attempt with proper data
        attempt = QuizAttempt.objects.create(
            user=request.user,
            quiz=quiz,
            score=score,
            max_score=max_score,
            time_taken=0  # TODO: Implement timer functionality
        )
        
        logger.info(f"Quiz attempt submitted: {attempt.id} by {request.user.username}")
        
        return render(request, "quiz/result.html", {
            "score": score, 
            "total": max_score,  # Use max_score instead of question count
            "quiz": quiz,
            "now": timezone.now(),
            "percentage": (score / max_score) * 100 if max_score > 0 else 0
        })
    except Exception as e:
        logger.error(f"Error submitting quiz: {str(e)}")
        return HttpResponseBadRequest("An error occurred while processing your submission")

def api_submit(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=400)
    
    try:
        data = request.POST
        score = 0
        total = Question.objects.count()
        
        # Process questions efficiently
        for q in Question.objects.all():
            selected = data.get(str(q.id))
            if selected:
                try:
                    if q.options.get(id=int(selected)).is_correct:
                        score += 1
                except (ValueError, q.options.model.DoesNotExist):
                    pass
        
        return JsonResponse({"score": score, "total": total})
    except Exception as e:
        logger.error(f"Error in API submit: {str(e)}")
        return JsonResponse({"error": "An error occurred"}, status=500)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            logger.info(f"New user registered: {user.username}")
            # TODO: Add success message
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'quiz/register.html', {'form': form})
