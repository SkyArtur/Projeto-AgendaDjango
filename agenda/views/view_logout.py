from django.shortcuts import redirect
from django.contrib import auth


def view_logout(request):
    auth.logout(request)
    return redirect('login')
