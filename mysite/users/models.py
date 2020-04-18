from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.EmailField()
    birth_date = models.DateField()
