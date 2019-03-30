from django.urls import path
from . import views as blog_views

urlpatterns = [
    path('', blog_views.index, name='blog_home'),
    # path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
]
