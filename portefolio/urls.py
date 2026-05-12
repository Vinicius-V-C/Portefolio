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

]