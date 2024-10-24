from django.urls import path

from wallet.views import WalletView, TransactionView, CoinListView

urlpatterns = [
    path('wallet/', WalletView.as_view(), name='wallet'),
    path('transaction/', TransactionView.as_view(), name='transaction'),
    path('coins/', CoinListView.as_view(), name='coin-list'),
]
