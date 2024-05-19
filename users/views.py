from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# View para o login do usuário
def login_view(request):
    if request.method == "POST":  # Se o método da requisição for POST
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)  # Autentica o usuário
        if user is not None:
            login(request, user)  # Realiza o login do usuário
            return redirect('home')  # Redireciona para a página inicial (ajuste conforme necessário)
        else:
            messages.error(request, 'Usuário ou senha inválidos')  # Exibe mensagem de erro
    return render(request, 'users/login.html')  # Renderiza o template de login

# View para o logout do usuário
def logout_view(request):
    logout(request)  # Realiza o logout do usuário
    return redirect('login')  # Redireciona para a página de login

# View para o registro de novos usuários
def register_view(request):
    if request.method == "POST":  # Se o método da requisição for POST
        form = UserCreationForm(request.POST)  # Instancia o formulário de criação de usuário com os dados enviados
        if form.is_valid():
            form.save()  # Salva o novo usuário no banco de dados
            messages.success(request, 'Conta criada com sucesso')  # Exibe mensagem de sucesso
            return redirect('login')  # Redireciona para a página de login
    else:
        form = UserCreationForm()  # Instancia um formulário vazio
    return render(request, 'users/register.html', {'form': form})  # Renderiza o template de registro com o formulário
