from django.contrib import admin
from .models import (
    Language,
    Programmer,
    Paradigm
)

admin.site.register(Language)
admin.site.register(Paradigm)
admin.site.register(Programmer)
