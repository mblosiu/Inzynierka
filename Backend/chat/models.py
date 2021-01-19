from django.db import models

# Create your models here.
from users.models import User


class Message(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, related_name='sender', default=None, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver', default=None, on_delete=models.CASCADE)
    message = models.CharField(max_length=30, null=True, blank=True, default=None)

    objects = models.Manager()
