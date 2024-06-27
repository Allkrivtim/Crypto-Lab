from django.db import models

class UserProfile(models.Model):
    telegram_id = models.CharField(max_length=100, unique=True)
    token_balance = models.PositiveIntegerField(default=0)
    knowledge_points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.telegram_id
