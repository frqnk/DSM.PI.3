from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate as auth, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from . import forms


def home_view(request):
    return render(request, 'core_app/home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Entrada bem sucedida.')
            return redirect('home')
        else:
            messages.error(request, 'Endereço de email ou senha inválido.')
    return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    messages.success(request, 'Saída bem sucedida.')
    return redirect('home')


def signup(request):
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = auth(username=email, password=password)
            login(request, user)
            messages.success(request, 'Cadastro bem sucedido.')
            return redirect('home')
        else:
            messages.error(request, 'Cadastro mal sucedido.')
    else:
        form = forms.SignupForm()
        return render(request, 'signup.html', {'form': form})
