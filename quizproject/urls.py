from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from quiz import views_auth, views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("quiz.urls")),
    path("register/", views_auth.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="quiz/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
