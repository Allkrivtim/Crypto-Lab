from django.db import models

class User(models.Model):
    telegram_id = models.CharField(max_length=100, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f'User {self.telegram_id}'

class UserIP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return f'{self.user.telegram_id} - {self.ip_address}'
