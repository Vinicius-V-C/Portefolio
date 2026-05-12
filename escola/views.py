
## ficheiro escola/views.py
from .models import Professor, Aluno
from django.shortcuts import render
from .models import Curso

def cursos_view(request):
    cursos=Curso.objects.all()       
    return render(request, 'escola/cursos.html', {'cursos': cursos})

def professores_view(request):
    professores = Professor.objects.prefetch_related('cursos').all()

    context = {
        'professores': professores
    }

    return render(request, 'escola/professores.html', context)

def alunos_view(request):
    alunos = Aluno.objects.prefetch_related('cursos').all()

    context = {
        'alunos': alunos
    }

    return render(request, 'escola/alunos.html', context)

def curso_view(request, id):
    curso=Curso.objects.get(id=id)       
    return render(request, 'escola/curso.html', {'curso': curso})    