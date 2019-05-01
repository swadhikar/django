from rest_framework import routers
from django.urls import path, include
from .views import (
    LanguageView,
    ParadigmView,
    ProgrammerView
)

router = routers.DefaultRouter()
router.register('languages', LanguageView)
router.register('paradigm', ParadigmView)
router.register('programmer', ProgrammerView)

urlpatterns = [
    path('', include(router.urls), name='language_view')
]
