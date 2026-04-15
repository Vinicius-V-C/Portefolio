from django.contrib import admin
from .models import (
    Licenciatura, Docente, UnidadeCurricular,
    Projeto, Tecnologia, Competencia,
    Formacao, ExperienciaProfissional, TFC, MakingOf
)

admin.site.register(Formacao)
admin.site.register(ExperienciaProfissional)
admin.site.register(TFC)
admin.site.register(MakingOf)
admin.site.register(Tecnologia)
admin.site.register(Competencia)
admin.site.register(Licenciatura)


class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'unidade_curricular')
    search_fields = ('nome',)


admin.site.register(Projeto, ProjetoAdmin)


class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'semestre')
    search_fields = ('nome',)


admin.site.register(UnidadeCurricular, UnidadeCurricularAdmin)


class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    search_fields = ('nome',)


admin.site.register(Docente, DocenteAdmin)