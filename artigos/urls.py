from django.urls import path
from . import views

urlpatterns = [

    path('', views.artigos_view, name='artigos'),

    path(
        'criar/',
        views.criar_artigo,
        name='criar_artigo'
    ),

]