import requests
import json
from config import keys


class APIException(Exception):
    pass


class CriptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == amount:
            raise APIException(f'Название валюты надо вводить буквами, как в образце. /help')
        elif base == amount:
            raise APIException(f'Название валюты надо вводить буквами, как в образце. /help')
        elif quote == base:
            raise APIException(f'Конвертируемые валюты должны быть различны.'\
                               f' Я не могу перевести валюту в саму себя! /help')
        else:
            ...
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Данной валюты "{quote}" нет в списке доступных валют. Проверьте, пожалуйста,'\
                               f' написание.  /values')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Данной валюты "{base}" нет в списке доступных валют. Проверьте, пожалуйста,'\
                               f'написание. /values')
        try:
            amount = float(amount)
            if amount <= 0:
                raise APIException(f'Я отрицательные значения или ноль конвертировать не умею! /help')
        except ValueError:
            raise APIException(f'"количество" надо вводить в виде числового значения. Дробные числа'\
                               f' пишутся через точку. /help')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]] * amount

        return total_base