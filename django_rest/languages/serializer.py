from rest_framework import serializers
from .models import (
    Language,
    Paradigm,
    Programmer
)


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'url', 'name', 'paradigm')


class ParadigmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paradigm
        fields = ('id', 'url', 'name')


class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programmer
        fields = ('id', 'url', 'name', 'languages')
