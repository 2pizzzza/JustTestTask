import json
from datetime import datetime

import requests
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer


class BitcoinPriceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        asyncio.create_task(self.monitor_price())

    async def disconnect(self, close_code):
        pass

    async def monitor_price(self):

        while True:
            price_message = self.get_bitcoin_price()
            await self.send(text_data=json.dumps(price_message))
            await asyncio.sleep(0.1)

    def get_bitcoin_price(self):

        try:
            url = "https://api.binance.com/api/v3/ticker/price"
            params = {"symbol": "BTCUSDT"}
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()
            data = response.json()
            price = float(data['price'])
            return {"timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "price": price}
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}
