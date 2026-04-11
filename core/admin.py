from django.contrib import admin
from .models import Licenciatura, Docente, UnidadeCurricular, Projeto, Tecnologia, Competencia

admin.site.register(Tecnologia)
admin.site.register(Competencia)
admin.site.register(Projeto)
admin.site.register(UnidadeCurricular)
admin.site.register(Docente)
admin.site.register(Licenciatura)