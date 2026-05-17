from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CriarUtilizadorForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from sesame.utils import get_query_string



def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'accounts/login.html')


def logout_view(request):

    logout(request)

    return redirect('home')


def registo_view(request):

    form = CriarUtilizadorForm()

    if request.method == 'POST':

        form = CriarUtilizadorForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('login')

    return render(request,
                  'accounts/registo.html',
                  {'form': form})


def magic_link(request):

    if request.method == 'POST':

        email = request.POST.get('email')

        try:

            user = User.objects.get(email=email)

            query_string = get_query_string(user)

            link = request.build_absolute_uri(
                '/sesame/login/' + query_string
            )

            send_mail(
                'Login mágico',
                f'Clique no link: {link}',
                'admin@localhost',
                [email],
                fail_silently=False,
            )

            return render(request,
                          'accounts/magic_enviado.html')

        except User.DoesNotExist:

            pass

    return render(request,
              'accounts/magic_link.html',
              {'enviado': True})                