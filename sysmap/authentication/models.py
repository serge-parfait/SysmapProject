from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class ROLE_CHOICES(models.TextChoices):
        CREATOR = 'CREATOR'
        GESTIONNAIRE_22 = 'GESTION22'
        GESTIONNAIRE_94 = 'GESTION94'
        SUPERVISEUR = 'SUPERVISOR'
        MEMBER_COMMISSION = 'MEMBER'
    role = models.fields.CharField(max_length=15, choices=ROLE_CHOICES.choices, verbose_name='Rôle', default="CREATOR")
    profile_photo = models.ImageField(verbose_name='Photo de profil')