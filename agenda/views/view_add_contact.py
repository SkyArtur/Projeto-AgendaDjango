from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.core.validators import ValidationError
from django.contrib.auth.decorators import login_required
from agenda.models import ContactModel, RelationshipModel


@login_required(redirect_field_name='login')
def view_add_contact(request):
    rel_model = RelationshipModel.objects.all()
    if request.method != 'POST':
        return render(request, 'pages/add_contact.html', {'relationship': rel_model})
    name = request.POST.get('name')
    lastname = request.POST.get('lastname')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    relationship = request.POST.get('relationship')
    details = request.POST.get('details')
    image = request.FILES.get('image')
    try:
        validate_email(email)
    except ValidationError:
        messages.error(request, 'Email inválido.')
        return render(request, 'pages/add_contact.html', {'relationship': rel_model})
    if not name or not phone:
        messages.error(request, 'Campos vazios ou dados inválidos.')
        return render(request, 'pages/add_contact.html', {'relationship': rel_model})
    elif ContactModel.objects.filter(email=email).exists():
        messages.error(request, 'Email já cadastrado.')
        return render(request, 'pages/add_contact.html', {'relationship': rel_model})
    elif ContactModel.objects.filter(phone=phone).exists():
        messages.error(request, 'Telefone já cadastrado.')
        return render(request, 'pages/add_contact.html', {'relationship': rel_model})
    else:
        contact = ContactModel.objects.create(
            name=name, lastname=lastname, email=email, phone=phone,
            relationship_id=relationship, details=details, image=image
        )
        contact.save()
        messages.success(request, 'Novo contato adicionado.')
        return redirect('contacts')

