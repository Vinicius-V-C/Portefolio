from django.shortcuts import render, redirect, get_object_or_404

from .models import (
    Projeto,
    Tecnologia,
    Competencia,
    Formacao
)

from .forms import (
    ProjetoForm,
    TecnologiaForm,
    CompetenciaForm,
    FormacaoForm
)

from django.contrib.auth.decorators import (
    login_required,
    user_passes_test
)


def gestor_portefolio(user):

    return user.is_authenticated and user.groups.filter(
        name='gestor-portefolio'
    ).exists()


# =========================
# PROJETOS
# =========================

def projetos_view(request):

    projetos = Projeto.objects.all()

    return render(
        request,
        'portefolio/projetos.html',
        {
            'projetos': projetos,
            'is_gestor': gestor_portefolio(request.user)
        }
    )


@login_required
@user_passes_test(gestor_portefolio)
def novo_projeto_view(request):

    form = ProjetoForm(
        request.POST or None,
        request.FILES or None
    )

    if form.is_valid():

        form.save()

        return redirect('projetos')

    return render(
        request,
        'portefolio/form.html',
        {'form': form}
    )


@login_required
@user_passes_test(gestor_portefolio)
def edita_projeto_view(request, projeto_id):

    projeto = get_object_or_404(
        Projeto,
        id=projeto_id
    )

    form = ProjetoForm(
        request.POST or None,
        request.FILES or None,
        instance=projeto
    )

    if form.is_valid():

        form.save()

        return redirect('projetos')

    return render(
        request,
        'portefolio/form.html',
        {
            'form': form,
            'projeto': projeto
        }
    )


@login_required
@user_passes_test(gestor_portefolio)
def apaga_projeto_view(request, projeto_id):

    projeto = get_object_or_404(
        Projeto,
        id=projeto_id
    )

    if request.method == 'POST':

        projeto.delete()

        return redirect('projetos')

    return render(
        request,
        'portefolio/confirmar_delete.html',
        {'objeto': projeto}
    )


# =========================
# TECNOLOGIAS
# =========================

def tecnologias_view(request):

    tecnologias = Tecnologia.objects.all()

    return render(
        request,
        'portefolio/tecnologias.html',
        {
            'tecnologias': tecnologias,
            'is_gestor': gestor_portefolio(request.user)
        }
    )


@login_required
@user_passes_test(gestor_portefolio)
def nova_tecnologia_view(request):

    form = TecnologiaForm(
        request.POST or None,
        request.FILES or None
    )

    if form.is_valid():

        form.save()

        return redirect('tecnologias')

    return render(
        request,
        'portefolio/form.html',
        {'form': form}
    )


@login_required
@user_passes_test(gestor_portefolio)
def edita_tecnologia_view(request, tecnologia_id):

    tecnologia = get_object_or_404(
        Tecnologia,
        id=tecnologia_id
    )

    form = TecnologiaForm(
        request.POST or None,
        request.FILES or None,
        instance=tecnologia
    )

    if form.is_valid():

        form.save()

        return redirect('tecnologias')

    return render(
        request,
        'portefolio/form.html',
        {'form': form}
    )


@login_required
@user_passes_test(gestor_portefolio)
def apaga_tecnologia_view(request, tecnologia_id):

    tecnologia = get_object_or_404(
        Tecnologia,
        id=tecnologia_id
    )

    if request.method == 'POST':

        tecnologia.delete()

        return redirect('tecnologias')

    return render(
        request,
        'portefolio/confirmar_delete.html',
        {'objeto': tecnologia}
    )


# =========================
# COMPETÊNCIAS
# =========================

def competencias_view(request):

    competencias = Competencia.objects.all()

    return render(
        request,
        'portefolio/competencias.html',
        {
            'competencias': competencias,
            'is_gestor': gestor_portefolio(request.user)
        }
    )


@login_required
@user_passes_test(gestor_portefolio)
def nova_competencia_view(request):

    form = CompetenciaForm(request.POST or None)

    if form.is_valid():

        form.save()

        return redirect('competencias')

    return render(
        request,
        'portefolio/form.html',
        {'form': form}
    )


@login_required
@user_passes_test(gestor_portefolio)
def edita_competencia_view(request, competencia_id):

    competencia = get_object_or_404(
        Competencia,
        id=competencia_id
    )

    form = CompetenciaForm(
        request.POST or None,
        instance=competencia
    )

    if form.is_valid():

        form.save()

        return redirect('competencias')

    return render(
        request,
        'portefolio/form.html',
        {'form': form}
    )


@login_required
@user_passes_test(gestor_portefolio)
def apaga_competencia_view(request, competencia_id):

    competencia = get_object_or_404(
        Competencia,
        id=competencia_id
    )

    if request.method == 'POST':

        competencia.delete()

        return redirect('competencias')

    return render(
        request,
        'portefolio/confirmar_delete.html',
        {'objeto': competencia}
    )


# =========================
# FORMAÇÕES
# =========================

def formacoes_view(request):

    formacoes = Formacao.objects.all()

    return render(
        request,
        'portefolio/formacoes.html',
        {
            'formacoes': formacoes,
            'is_gestor': gestor_portefolio(request.user)
        }
    )


@login_required
@user_passes_test(gestor_portefolio)
def nova_formacao_view(request):

    form = FormacaoForm(request.POST or None)

    if form.is_valid():

        form.save()

        return redirect('formacoes')

    return render(
        request,
        'portefolio/form.html',
        {'form': form}
    )


@login_required
@user_passes_test(gestor_portefolio)
def edita_formacao_view(request, formacao_id):

    formacao = get_object_or_404(
        Formacao,
        id=formacao_id
    )

    form = FormacaoForm(
        request.POST or None,
        instance=formacao
    )

    if form.is_valid():

        form.save()

        return redirect('formacoes')

    return render(
        request,
        'portefolio/form.html',
        {'form': form}
    )


@login_required
@user_passes_test(gestor_portefolio)
def apaga_formacao_view(request, formacao_id):

    formacao = get_object_or_404(
        Formacao,
        id=formacao_id
    )

    if request.method == 'POST':

        formacao.delete()

        return redirect('formacoes')

    return render(
        request,
        'portefolio/confirmar_delete.html',
        {'objeto': formacao}
    )


# =========================
# SOBRE
# =========================

def sobre_view(request):

    tecnologias = Tecnologia.objects.all()

    texto_markdown = """
## Problemas encontrados
- TemplateDoesNotExist
- Erros de migrations
- Problemas com ForeignKey

## Aprendizagens
- Compreensão do MVT
- Uso de migrations
- Uso do markdownify

## Tecnologias usadas
- Django
- HTML
- CSS
- GitHub
"""

    return render(
        request,
        'portefolio/sobre.html',
        {
            'tecnologias': tecnologias,
            'texto_markdown': texto_markdown,
        }
    )