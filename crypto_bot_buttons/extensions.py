import requests
import json
from config import keys


class MYException(Exception):
    pass

class MYConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise MYException(f'Невозможно обработать одинаковые валюты "{base}"')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise MYException(f'Введите правильное значение валюты "{base}"')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise MYException(f'Введите правильное значение валюты "{quote}"')

        try:
            amount = float(amount)
        except ValueError:
            raise MYException(f'Введите количество обрабатываемой валюты "{amount}"')

        if amount <= 0:
            raise MYException(f'Введено не верное колличество валюты {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]] * float(amount)

        return total_base