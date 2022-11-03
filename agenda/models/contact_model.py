from django.db import models
from django.utils import timezone
from agenda.models.relationship_model import RelationshipModel


class ContactModel(models.Model):
    name = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=25)
    email = models.EmailField(max_length=150, blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    relationship = models.ForeignKey(RelationshipModel, on_delete=models.DO_NOTHING)
    details = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='imgs_contacts', blank=True, null=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
