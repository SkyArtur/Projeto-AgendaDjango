from django.shortcuts import redirect
from django.contrib import messages
from agenda.models import ContactModel


def view_delete(request, id_contact):
    contact = ContactModel.objects.get(id=id_contact)
    messages.warning(request, f'{contact.name} {contact.lastname} | Contato removido.')
    contact.delete()
    return redirect('contacts')
