from django.shortcuts import render, get_object_or_404
from agenda.models import ContactModel


def view_detail(request, id_contact):
    contact = get_object_or_404(ContactModel, id=id_contact)
    return render(request, 'pages/detail.html', {'contact': contact})
