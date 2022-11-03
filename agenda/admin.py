from django.contrib import admin
from .models import ContactModel, RelationshipModel

# Register your models here.
admin.site.register(RelationshipModel)
admin.site.register(ContactModel)
