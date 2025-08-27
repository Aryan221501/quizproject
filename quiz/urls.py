from django.urls import path
from . import views
from . import views_api

urlpatterns = [
    path("", views.home, name="home"),
    path("quizzes/", views.quiz_list, name="quiz_list"),
    path("quiz/<int:quiz_id>/", views.quiz_detail, name="quiz_detail"),
    path("quiz/history/", views.quiz_history, name="quiz_history"),
    path("leaderboard/", views.leaderboard, name="leaderboard"),
    path("profile/", views.profile, name="profile"),
    path("submit/", views.submit, name="submit"),
    path("api/submit/", views.api_submit, name="api_submit"),
    # API endpoints
    path("api/categories/", views_api.CategoryListCreateView.as_view(), name="category-list"),
    path("api/categories/<int:pk>/", views_api.CategoryDetailView.as_view(), name="category-detail"),
    path("api/quizzes/", views_api.QuizListCreateView.as_view(), name="quiz-list"),
    path("api/quizzes/<int:pk>/", views_api.QuizDetailView.as_view(), name="quiz-detail"),
    path("api/quizzes/<int:quiz_id>/submit/", views_api.submit_quiz, name="api-submit-quiz"),
    path("api/attempts/", views_api.QuizAttemptListCreateView.as_view(), name="attempt-list"),
]
