from rest_framework import viewsets
from django.shortcuts import render
from .serializer import (
    LanguageSerializer,
    ParadigmSerializer,
    ProgrammerSerializer
)
from .models import (
    Language,
    Paradigm,
    Programmer
)


class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer


class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer
