from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from .models import Category, Quiz, Question, Option, QuizAttempt
from .serializers import CategorySerializer, QuizSerializer, QuestionSerializer, OptionSerializer, QuizAttemptSerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]  # Allow public access

class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]  # Allow public access

class QuizListCreateView(generics.ListCreateAPIView):
    queryset = Quiz.objects.filter(is_active=True)
    serializer_class = QuizSerializer
    permission_classes = [AllowAny]  # Allow public access

class QuizDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.filter(is_active=True)
    serializer_class = QuizSerializer
    permission_classes = [AllowAny]  # Allow public access

@api_view(['POST'])
def submit_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id, is_active=True)
    user = request.user
    score = 0
    
    # Get the submitted answers
    answers = request.data.get('answers', {})
    
    # Calculate score
    for question_id, option_id in answers.items():
        try:
            question = Question.objects.get(id=question_id, quiz=quiz)
            selected_option = Option.objects.get(id=option_id, question=question)
            if selected_option.is_correct:
                score += 1
        except (Question.DoesNotExist, Option.DoesNotExist):
            pass  # Invalid question or option, skip it
    
    # Save the attempt
    attempt = QuizAttempt.objects.create(
        user=user,
        quiz=quiz,
        score=score
    )
    
    return Response({
        'score': score,
        'total': quiz.questions.count(),
        'attempt_id': attempt.id
    }, status=status.HTTP_201_CREATED)

class QuizAttemptListCreateView(generics.ListCreateAPIView):
    serializer_class = QuizAttemptSerializer
    
    def get_queryset(self):
        return QuizAttempt.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)