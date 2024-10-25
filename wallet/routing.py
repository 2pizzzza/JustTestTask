from django.urls import path, re_path

from .consumers import BitcoinPriceConsumer

websocket_urlpatterns = [
    path('ws/bitcoin_price/', BitcoinPriceConsumer.as_asgi()),
]
