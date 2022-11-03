from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from agenda.models import ContactModel


@login_required(redirect_field_name='login')
def view_contacts(request):
    contacts = ContactModel.objects.all()
    return render(request, 'pages/contacts.html', {'contacts': contacts})

