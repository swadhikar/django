from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.contact),
    path('snippet/', views.snippet_details)
]
