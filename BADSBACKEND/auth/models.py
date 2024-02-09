from django.db import models

# Create your models here.


class AllergyUsers(models.Model):

    name = models.CharField(max_length=100)
    eth_address = models.CharField(max_length=100)
    family_history = models.CharField(max_length=100)
    genotype = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=100)
    allergy = models.CharField(max_length=100)
    medical_history = models.CharField(max_length=100)

    class Meta:
        app_label = 'auth'

    def __str__(self):
        return self.name
