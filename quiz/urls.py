from django.urls import path
from . import views

urlpatterns = [
    path("", views.quiz_view, name="quiz"),
    path("submit/", views.submit, name="submit"),
    path("api/submit/", views.api_submit, name="api_submit"),
]
