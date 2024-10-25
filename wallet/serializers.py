from rest_framework import serializers
from .models import Wallet, WalletCoin, Transaction, Coin


class TransactionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'coin', 'amount', 'price', 'transaction_type', 'created_at']


class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = ['id', 'name']


class WalletCoinSerializer(serializers.ModelSerializer):
    coin_name = serializers.CharField(source='coin.name')

    class Meta:
        model = WalletCoin
        fields = ['coin_name', 'balance']


class WalletSerializer(serializers.ModelSerializer):
    coins = WalletCoinSerializer(many=True, read_only=True)

    class Meta:
        model = Wallet
        fields = ['usdt_balance', 'coins']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['coin', 'amount', 'price', 'transaction_type']

    def create(self, validated_data):
        wallet = self.context['wallet']
        coin = validated_data['coin']
        amount = validated_data['amount']
        price = validated_data['price']
        transaction_type = validated_data['transaction_type']

        if transaction_type == 'BUY':
            total_cost = price * amount
            if wallet.usdt_balance < total_cost:
                raise serializers.ValidationError('Недостаточно средств для покупки')

            wallet.usdt_balance -= total_cost
            wallet.save()

            wallet_coin, created = WalletCoin.objects.get_or_create(wallet=wallet, coin=coin)
            wallet_coin.balance += amount
            wallet_coin.save()

        elif transaction_type == 'SELL':
            wallet_coin = WalletCoin.objects.get(wallet=wallet, coin=coin)

            if wallet_coin.balance < amount:
                raise serializers.ValidationError('Недостаточно криптовалюты для продажи')

            total_gain = price * amount
            wallet.usdt_balance += total_gain
            wallet.save()

            wallet_coin.balance -= amount
            wallet_coin.save()

        transaction = Transaction.objects.create(
            wallet=wallet,
            coin=coin,
            amount=amount,
            price=price,
            transaction_type=transaction_type
        )
        return transaction
