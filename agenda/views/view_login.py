from django.shortcuts import render, redirect
from django.contrib import messages, auth


def view_login(request):
    if request.method != 'POST':
        return render(request, 'pages/login.html')
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(request, username=username, password=password)
    if not user:
        messages.error(request, 'Dados inválidos.')
        return render(request, 'pages/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Login com sucesso.')
        return redirect('contacts')
