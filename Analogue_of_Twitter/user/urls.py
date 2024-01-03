from django.urls import path
from .endpoints import RegisterView, LoginView



urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]