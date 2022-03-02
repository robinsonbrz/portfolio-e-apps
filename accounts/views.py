from django.contrib import messages
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.shortcuts import redirect, render

# Create your views here.


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return render(request, 'accounts/logout.html')


def cadastro(request):
    if request.method != 'POST':
        return render(request, 'accounts/cadastro.html')
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')
    if not nome or not sobrenome or not email or not usuario or not \
                senha or not senha2:
        messages.error(request, 'Nenhum campo pode estar vazio.')
        return render(request, 'accounts/cadastro.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'Email inválido.')
        return render(request, 'accounts/cadastro.html')        
    
    if len(senha) < 6:
        messages.error(request, 'Senha precisa ter mais que 5 caracteres.')
        return render(request, 'accounts/cadastro.html')    

    if len(usuario) < 6:
        messages.error(request, 'Usuario precisa ter mais que 5 caracteres.')
        return render(request, 'accounts/cadastro.html')            

    if senha != senha2:
        messages.error(request, 'Senhas digitadas precisam ser iguais.')
        return render(request, 'accounts/cadastro.html')  

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuário já existe.')
        return render(request, 'accounts/cadastro.html')  

    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email já existe.')
        return render(request, 'accounts/cadastro.html')  

    messages.success(request, 'Registrado com sucesso! Agora faça o login.')

    user = User.objects.create_user(username=usuario, email=email,
                                    password=senha, first_name=nome,
                                    last_name=sobrenome)
    user.save()
    return redirect('login')

    # messages.info(request, 'Nada postado.')
    # print(request.POST)
    
    
def dashboard(request):
    return render(request, 'accounts/dashboard.html')