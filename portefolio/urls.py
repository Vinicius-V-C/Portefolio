from django.urls import path
from . import views

urlpatterns = [

    path('licenciaturas/', views.licenciaturas_view, name='licenciaturas'),
    path('docentes/', views.docentes_view, name='docentes'),
    path('ucs/', views.ucs_view, name='ucs'),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('competencias/', views.competencias_view, name='competencias'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('formacoes/', views.formacoes_view, name='formacoes'),
    path('experiencias/', views.experiencias_view, name='experiencias'),
    path('tfcs/', views.tfcs_view, name='tfcs'),
    path('makingof/', views.makingof_view, name='makingof'),
    path('projetos/criar/', views.criar_projeto, name='criar_projeto'),
    path('projetos/editar/<int:projeto_id>/', views.editar_projeto, name='editar_projeto'),
    path('projetos/apagar/<int:projeto_id>/', views.apagar_projeto, name='apagar_projeto'),
    path('tecnologias/criar/', views.criar_tecnologia, name='criar_tecnologia'),
    path('tecnologias/editar/<int:tecnologia_id>/', views.editar_tecnologia, name='editar_tecnologia'),
    path('tecnologias/apagar/<int:tecnologia_id>/', views.apagar_tecnologia, name='apagar_tecnologia'),
    path('competencias/criar/', views.criar_competencia, name='criar_competencia'),
    path('competencias/editar/<int:competencia_id>/', views.editar_competencia, name='editar_competencia'),
    path('competencias/apagar/<int:competencia_id>/', views.apagar_competencia, name='apagar_competencia'),
    path('formacoes/criar/', views.criar_formacao, name='criar_formacao'),
    path('formacoes/editar/<int:formacao_id>/', views.editar_formacao, name='editar_formacao'),
    path('formacoes/apagar/<int:formacao_id>/', views.apagar_formacao, name='apagar_formacao'),
    path('sobre/', views.sobre, name='sobre'),
    path('makingof/', views.makingof, name='makingof'),

]