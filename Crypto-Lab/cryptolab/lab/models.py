from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token_balance = models.PositiveIntegerField(default=0)
    knowledge_points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username
