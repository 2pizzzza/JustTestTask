from django.db import models
from django.conf import settings


class Coin(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class Wallet(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    usdt_balance = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    def __str__(self):
        return f"Wallet of {self.user.name}"


class WalletCoin(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='coins')
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=20, decimal_places=8, default=0)

    class Meta:
        unique_together = ('wallet', 'coin')

    def __str__(self):
        return f"{self.coin.name}: {self.balance} (Wallet of {self.wallet.user.name})"


class Transaction(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    transaction_type = models.CharField(max_length=4, choices=(('BUY', 'Buy'), ('SELL', 'Sell')))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} {self.amount} {self.coin.name} by {self.wallet.user.name}"
