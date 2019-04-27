from django.urls import path
from . import views as blog_views

urlpatterns = [
    path('', blog_views.index, name='blog_home'),
    path('create/', blog_views.create_post, name='blog_create'),
    path('delete/<int:id>', blog_views.delete_post, name='blog_delete'),
    path('update/<int:id>', blog_views.update_post, name='blog_update'),
]
