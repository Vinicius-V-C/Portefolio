from django.contrib import admin
from .models import Licenciatura, Docente, UnidadeCurricular

admin.site.register(UnidadeCurricular)
admin.site.register(Docente)
admin.site.register(Licenciatura)