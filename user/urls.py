from django.urls import path, include
from .views import register, user_logout, user_login, user_profile

urlpatterns = [
    path('register/', register, name='register'),
    path("logout/", user_logout, name='logout'), 
    path("login/", user_login, name='user_login'), 
    path("user_profile/", user_profile, name='user_profile'), 
]