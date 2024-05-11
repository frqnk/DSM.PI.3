from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirecionar para uma página de sucesso
                return redirect('pagina_de_sucesso')
            else:
                # Exibir uma mensagem de erro caso o login falhe
                return render(request, 'login.html', {'form': form, 'erro': True})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirecionar para uma página de sucesso
            return redirect('pagina_de_sucesso')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

