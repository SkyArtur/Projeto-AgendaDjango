from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email, ValidationError
from django.contrib.auth.models import User


def view_add_new_user(request):
    if request.method != 'POST':
        return render(request, 'pages/add_new_user.html')
    for inputs in request.POST.values():
        if inputs is None or not inputs:
            messages.error(request, 'Não deixe campos vazios.')
            return render(request, 'pages/add_new_user.html')
    name = request.POST.get('name')
    lastname = request.POST.get('lastname')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirm = request.POST.get('confirm')
    try:
        validate_email(email)
        if User.objects.filter(username=email).exists():
            messages.error(request, 'Email já cadastrado!')
            return render(request, 'pages/add_new_user.html')
    except ValidationError:
        messages.error(request, 'Email inválido!')
        return render(request, 'pages/add_new_user.html')
    if password != confirm or len(password) < 6:
        if len(password) < 6:
            messages.error(request, 'A senha deve ter ao menos 6 caracteres!')
        else:
            messages.error(request, 'Senhas não conferem!')
        return render(request, 'pages/add_new_user.html')
    user = User.objects.create_user(
        first_name=name,
        last_name=lastname,
        username=email,
        password=password
    )
    user.save()
    messages.success(request, 'Novo usuário cadastrado com sucesso!')
    return redirect('login')
