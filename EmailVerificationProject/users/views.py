from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import UserRegistrationForm
from .models import User
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registrado com sucesso! Verifique seu email para ativar sua conta.')
            return redirect('verify_email')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def verify_email(request):                                                                                                  
    if request.method == 'POST':
        email = request.POST['email']
        code = request.POST['code']
        try:
            user = User.objects.get(email=email, verification_code=code)
            user.is_active = True
            user.verification_code = ''
            user.save()
            messages.success(request, 'Email verificado com sucesso! Você pode fazer login agora.')
            return redirect('login')
        except User.DoesNotExist:
            messages.error(request, 'Código de verificação inválido. Tente novamente.')
    return render(request, 'verify_email.html')

def resend_code(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
            user.verification_code = str(random.randint(1000, 9999))
            user.save()
            user.email_user('Seu novo código de verificação', f'Seu novo código é: {user.verification_code}')
            messages.success(request, 'Um novo código de verificação foi enviado.')
        except User.DoesNotExist:
            messages.error(request, 'Email não encontrado. Tente novamente.')
    return redirect('verify_email')
