from django.db import models
from django.conf import settings


from django.db import models
from django.conf import settings

class Wallet(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    btcusdt_balance = models.DecimalField(max_digits=20, decimal_places=8, default=0)

    def __str__(self):
        return f"{self.user.name}'s Wallet"


class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('buy', 'Buy'),
        ('sell', 'Sell'),
    )

    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    transaction_type = models.CharField(max_length=4, choices=TRANSACTION_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type.capitalize()} {self.amount} BTCUSDT for {self.wallet.user.name}"
