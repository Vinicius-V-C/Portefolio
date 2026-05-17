from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib.auth.decorators import login_required

from .models import Artigo
from .forms import ArtigoForm


def artigos_view(request):

    artigos = Artigo.objects.all()

    return render(
        request,
        'artigos/artigos.html',
        {'artigos': artigos}
    )


@login_required
def criar_artigo(request):

    if request.method == 'POST':

        form = ArtigoForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            artigo = form.save(commit=False)

            artigo.autor = request.user

            artigo.save()

            return redirect('artigos')

    else:

        form = ArtigoForm()

    return render(
        request,
        'artigos/form.html',
        {'form': form}
    )