from django.db import models


class RelationshipModel(models.Model):
    relationship = models.CharField(max_length=100)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.relationship
