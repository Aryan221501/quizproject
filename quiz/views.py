from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Question

def quiz_view(request):
    questions = Question.objects.prefetch_related("options").all()
    return render(request, "quiz/quiz.html", {"questions": questions})

def submit(request):
    if request.method == "POST":
        score = 0
        total = Question.objects.count()
        for q in Question.objects.all():
            selected = request.POST.get(str(q.id))
            if selected:
                try:
                    if q.options.get(id=int(selected)).is_correct:
                        score += 1
                except:
                    pass
        return render(request, "quiz/result.html", {"score": score, "total": total})
    return redirect("quiz")

def api_submit(request):
    if request.method == "POST":
        data = request.POST
        score = 0
        total = Question.objects.count()
        for q in Question.objects.all():
            selected = data.get(str(q.id))
            if selected:
                try:
                    if q.options.get(id=int(selected)).is_correct:
                        score += 1
                except:
                    pass
        return JsonResponse({"score": score, "total": total})
    return JsonResponse({"error": "POST required"}, status=400)
