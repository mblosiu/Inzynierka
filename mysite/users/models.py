from django.db import models

# Create your models here.

class UserData(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.EmailField()
    birth_date = models.DateField()
