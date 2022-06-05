from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, user_logout, user_login, user_profile

urlpatterns = [
    path('register/', register, name='register'),
    path("logout/", user_logout, name='logout'), 
    path("login/", user_login, name='user_login'), 
    path("user_profile/", user_profile, name='user_profile'), 
    path("reset_password/", auth_views.PasswordResetView.as_view(template_name="user/reset_password.html"), name='reset_password'), 
]