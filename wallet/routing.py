from django.urls import path, re_path

from .consumers import BitcoinPriceConsumer

websocket_urlpatterns = [
    re_path(r'^ws/bitcoin_price/$', BitcoinPriceConsumer.as_asgi()),
]
