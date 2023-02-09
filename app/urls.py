from django.urls import path
from app import views as chat_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("",chat_views.ChatPage, name="chat-page"),
    path("login/",LoginView.as_view(template_name="registration/login.html"),name="login-user"),
    path("auth/logout/",LogoutView.as_view(),name="logout-user"),
]