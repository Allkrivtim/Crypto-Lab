from django.db import models

class User(models.Model):
    telegram_id = models.CharField(max_length=100, unique=True)
    tokens = models.IntegerField(default=0)  # Добавление поля tokens

    def __str__(self):
        return self.telegram_id
