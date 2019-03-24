from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LoginView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
]
