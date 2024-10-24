from wallet.models import Transaction
from rest_framework import serializers
from .models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['id', 'user', 'btcusdt_balance']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['amount', 'transaction_type']

    def create(self, validated_data):
        wallet = validated_data['wallet']
        transaction_type = validated_data['transaction_type']
        amount = validated_data['amount']

        if transaction_type == 'buy':
            wallet.btcusdt_balance += amount
        elif transaction_type == 'sell':
            if wallet.btcusdt_balance < amount:
                raise serializers.ValidationError("Insufficient balance to sell.")
            wallet.btcusdt_balance -= amount

        wallet.save()
        return super().create(validated_data)
