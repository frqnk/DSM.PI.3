from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate as auth, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home.html')

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
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        messages.success(request, 'Cadastro bem sucedido.')
        return redirect('home')
    return render(request, 'signup.html')
