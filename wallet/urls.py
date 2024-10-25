from django.urls import path

from wallet.views import WalletView, TransactionView, CoinListView, UserTransactionsView

urlpatterns = [
    path('wallet/', WalletView.as_view(), name='wallet'),
    path('transaction/', TransactionView.as_view(), name='transaction'),
    path('coins/', CoinListView.as_view(), name='coin-list'),
    path('transactions/', UserTransactionsView.as_view(), name='user-transactions'),
]
