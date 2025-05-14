from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, CadastrarForm
from .models import Role, Usuario

# Create your views here.
def home_view(request):
    if not request.user.is_authenticated:
        return redirect('usuario_login')

    user = request.user
    usuario = None
    try:
        usuario = Usuario.objects.get(user=user)
    except Usuario.DoesNotExist:
        usuario = None

    return render(request, 'home.html', {'usuario': usuario})

def usuario_login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('usuario_painel')
            else:
                print('USUÁRIO INVÁLIDO')
                pass 
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

@login_required
def usuario_cadastrar_view(request):
    if request.method == 'POST':
        form = CadastrarForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']

            # Criar o User do Django
            user = User.objects.create_user(username=username, password=password)

            # Criar o Usuario relacionado ao User e Role
            usuario = Usuario.objects.create(user=user, role=role)

            return redirect('usuario_login') # Redirect to login page after registration
    else:
        form = CadastrarForm()

    user = request.user

    try:
        usuario = Usuario.objects.get(user=user)
    except Usuario.DoesNotExist:
        usuario = None

    return render(request, 'cadastrar.html', {'form': form, 'usuario': usuario})

@login_required
def usuario_listar_view(request):
    usuarios = Usuario.objects.all()
    user = request.user

    try:
        usuario = Usuario.objects.get(user=user)
    except Usuario.DoesNotExist:
        usuario = None
    return render(request, 'listar.html', {'usuarios': usuarios, 'usuario':usuario})

@login_required
def usuario_painel_view(request):
    user = request.user

    try:
        usuario = Usuario.objects.get(user=user)
    except Usuario.DoesNotExist:
        usuario = None

    return render(request, 'painel.html', {'usuario': usuario})

def usuario_logout_view(request):
    logout(request)
    return redirect('home')