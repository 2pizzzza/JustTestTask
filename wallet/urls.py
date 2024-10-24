from django.urls import path

from wallet.views import TransactionCreateView, WalletDetailView

urlpatterns = [
    path('transactions/', TransactionCreateView.as_view(), name='create_transaction'),
    path('wallet/', WalletDetailView.as_view(), name='wallet_detail'),
]
