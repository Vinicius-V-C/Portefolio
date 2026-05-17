from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import (
    Licenciatura,
    Docente,
    UnidadeCurricular,
    Tecnologia,
    Competencia,
    Projeto,
    Formacao,
    ExperienciaProfissional,
    TFC,
    MakingOf
)
from .forms import (
    ProjetoForm,
    TecnologiaForm,
    CompetenciaForm,
    FormacaoForm
)




def licenciaturas_view(request):
    licenciaturas = Licenciatura.objects.all()

    return render(request, 'portefolio/licenciaturas.html', {
        'licenciaturas': licenciaturas
    })


def docentes_view(request):
    docentes = Docente.objects.all()

    return render(request, 'portefolio/docentes.html', {
        'docentes': docentes
    })


def ucs_view(request):
    ucs = UnidadeCurricular.objects.select_related(
        'licenciatura'
    ).prefetch_related(
        'docentes'
    )

    return render(request, 'portefolio/ucs.html', {
        'ucs': ucs
    })


def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all()

    return render(request, 'portefolio/tecnologias.html', {
        'tecnologias': tecnologias
    })


def competencias_view(request):
    competencias = Competencia.objects.all()

    return render(request, 'portefolio/competencias.html', {
        'competencias': competencias
    })


def projetos_view(request):
    projetos = Projeto.objects.select_related(
        'unidade_curricular'
    ).prefetch_related(
        'tecnologias',
        'competencias'
    )

    return render(request, 'portefolio/projetos.html', {
        'projetos': projetos
    })


def formacoes_view(request):
    formacoes = Formacao.objects.prefetch_related(
        'competencias'
    )

    return render(request, 'portefolio/formacoes.html', {
        'formacoes': formacoes
    })


def experiencias_view(request):
    experiencias = ExperienciaProfissional.objects.prefetch_related(
        'competencias'
    )

    return render(request, 'portefolio/experiencias.html', {
        'experiencias': experiencias
    })


def tfcs_view(request):
    tfcs = TFC.objects.all()

    return render(request, 'portefolio/tfcs.html', {
        'tfcs': tfcs
    })


def makingof_view(request):
    makingofs = MakingOf.objects.select_related(
        'projeto',
        'tecnologia',
        'unidade_curricular'
    )

    return render(request, 'portefolio/makingof.html', {
        'makingofs': makingofs
    })

@login_required
def criar_projeto(request):

    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('projetos')

    else:
        form = ProjetoForm()

    return render(request, 'portefolio/form.html', {
        'form': form,
        'titulo': 'Criar Projeto'
    }) 

@login_required
def editar_projeto(request, projeto_id):

    projeto = get_object_or_404(Projeto, id=projeto_id)

    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES, instance=projeto)

        if form.is_valid():
            form.save()
            return redirect('projetos')

    else:
        form = ProjetoForm(instance=projeto)

    return render(request, 'portefolio/form.html', {
        'form': form,
        'titulo': 'Editar Projeto'
    })

@login_required
def apagar_projeto(request, projeto_id):

    projeto = get_object_or_404(Projeto, id=projeto_id)

    if request.method == 'POST':
        projeto.delete()
        return redirect('projetos')

    return render(request, 'portefolio/confirmar_delete.html', {
        'objeto': projeto
    })           

@login_required
def criar_tecnologia(request):

    if request.method == 'POST':
        form = TecnologiaForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('tecnologias')

    else:
        form = TecnologiaForm()

    return render(request, 'portefolio/form.html', {
        'form': form,
        'titulo': 'Criar Tecnologia'
    })


@login_required
def editar_tecnologia(request, tecnologia_id):

    tecnologia = get_object_or_404(Tecnologia, id=tecnologia_id)

    if request.method == 'POST':
        form = TecnologiaForm(request.POST, request.FILES, instance=tecnologia)

        if form.is_valid():
            form.save()
            return redirect('tecnologias')

    else:
        form = TecnologiaForm(instance=tecnologia)

    return render(request, 'portefolio/form.html', {
        'form': form,
        'titulo': 'Editar Tecnologia'
    })


@login_required
def apagar_tecnologia(request, tecnologia_id):

    tecnologia = get_object_or_404(Tecnologia, id=tecnologia_id)

    if request.method == 'POST':
        tecnologia.delete()
        return redirect('tecnologias')

    return render(request, 'portefolio/confirmar_delete.html', {
        'objeto': tecnologia
    })

@login_required
def criar_competencia(request):

    if request.method == 'POST':
        form = CompetenciaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('competencias')

    else:
        form = CompetenciaForm()

    return render(request, 'portefolio/form.html', {
        'form': form,
        'titulo': 'Criar Competência'
    })


@login_required
def editar_competencia(request, competencia_id):

    competencia = get_object_or_404(Competencia, id=competencia_id)

    if request.method == 'POST':
        form = CompetenciaForm(request.POST, instance=competencia)

        if form.is_valid():
            form.save()
            return redirect('competencias')

    else:
        form = CompetenciaForm(instance=competencia)

    return render(request, 'portefolio/form.html', {
        'form': form,
        'titulo': 'Editar Competência'
    })


@login_required
def apagar_competencia(request, competencia_id):

    competencia = get_object_or_404(Competencia, id=competencia_id)

    if request.method == 'POST':
        competencia.delete()
        return redirect('competencias')

    return render(request, 'portefolio/confirmar_delete.html', {
        'objeto': competencia
    })

@login_required
def criar_formacao(request):

    if request.method == 'POST':
        form = FormacaoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('formacoes')

    else:
        form = FormacaoForm()

    return render(request, 'portefolio/form.html', {
        'form': form,
        'titulo': 'Criar Formação'
    })


@login_required
def editar_formacao(request, formacao_id):

    formacao = get_object_or_404(Formacao, id=formacao_id)

    if request.method == 'POST':
        form = FormacaoForm(request.POST, instance=formacao)

        if form.is_valid():
            form.save()
            return redirect('formacoes')

    else:
        form = FormacaoForm(instance=formacao)

    return render(request, 'portefolio/form.html', {
        'form': form,
        'titulo': 'Editar Formação'
    })


@login_required
def apagar_formacao(request, formacao_id):

    formacao = get_object_or_404(Formacao, id=formacao_id)

    if request.method == 'POST':
        formacao.delete()
        return redirect('formacoes')

    return render(request, 'portefolio/confirmar_delete.html', {
        'objeto': formacao
    })
    
def sobre(request):
    return render(request, 'portefolio/sobre.html')
        

def makingof(request):

    texto = """
# Título Markdown

## Sub-título

- item 1
- item 2

**bold**
"""

    return render(request,
                  'portefolio/makingof.html',
                  {'texto': texto})    