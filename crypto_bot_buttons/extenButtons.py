import requests
import json
from config import keys

class MyExceptionButtons(Exception):
    pass

class ConvertButtons:
    @staticmethod
    def get_quote(quote: str):
        if quote not in keys.values():
            raise MyExceptionButtons(f'Валюта выбрана не верно "{quote}"')
        return quote

    @staticmethod
    def get_base(quote: str, base: str):
        if quote == base:
            raise MyExceptionButtons(f'Невозможно перевести одинаковые валюты "{base}".')
        elif base not in keys.values():
            raise MyExceptionButtons(f'Валюта выбрана не верно "{base}".')
        return base, quote

    @staticmethod
    def get_total(quote: str, base: str, amount: str):
        try:
            amount = float(amount)
            # if amount > 0:
            #     raise MyExceptionButtons(f'Введено не верное колличество валюты {amount}')
        except ValueError:
            raise MyExceptionButtons(f'Введено не верное колличество валюты {amount}')

        if amount <= 0:
            raise MyExceptionButtons(f'Введено не верное колличество валюты {amount}')


        j = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote}&tsyms={base}')
        total_base = json.loads(j.content)
        total = total_base[base] * float(amount)

        return total