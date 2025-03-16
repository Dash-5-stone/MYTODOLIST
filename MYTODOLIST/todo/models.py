from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.username

class Tache(models.Model):
    STATUS_CHOICES = [
        ('a_faire', 'A faire'),
        ('en_cours', 'En cours'),
        ('termine', 'Terminé'),
    ]
    tache = models.CharField(max_length=200)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_limite = models.DateField(null=True, blank=True)  
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='a_faire')

    def __str__(self):
        return self.tache