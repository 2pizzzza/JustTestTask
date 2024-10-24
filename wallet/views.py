from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from wallet.models import Wallet
from wallet.serializers import TransactionSerializer, WalletSerializer


class TransactionCreateView(generics.CreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        wallet = Wallet.objects.get(user=self.request.user)
        serializer.save(wallet=wallet)


class WalletDetailView(generics.RetrieveAPIView):
    serializer_class = WalletSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return Wallet.objects.get(user=self.request.user)
