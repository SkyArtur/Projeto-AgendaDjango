from django.shortcuts import render, redirect
from django.db.models.functions import Concat
from django.db.models import Q, Value
from django.contrib import messages
from agenda.models import ContactModel


def view_search(request):
    term = request.GET.get('term')
    if term is None or not term:
        return redirect('contacts')
    _name = Concat('name', Value(' '), 'lastname')
    contact = ContactModel.objects.annotate(
        complete_name=_name,
    ).filter(
        Q(complete_name__icontains=term) | Q(phone__icontains=term) | Q(email__icontains=term)
    )
    if contact is None or not contact:
        messages.error(request, 'Nenhum contato encontrado.')
    return render(request, 'pages/contacts.html', {'contacts': contact})
