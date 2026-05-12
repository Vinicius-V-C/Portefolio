from django.shortcuts import render

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