from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Wallet, Coin, WalletCoin

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_wallet_for_new_user(sender, instance, created, **kwargs):
    if created:
        wallet = Wallet.objects.create(user=instance, usdt_balance=1000)

        popular_coins = ["BTC", "ETH", "LTC", "XRP", "ADA"]
        for coin_name in popular_coins:
            coin, _ = Coin.objects.get_or_create(name=coin_name)
            WalletCoin.objects.create(wallet=wallet, coin=coin, balance=0)
