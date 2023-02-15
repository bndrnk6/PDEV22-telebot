import json
import requests
from config import exchanges


class APIException(Exception):
    pass


class Convertor:
    @staticmethod
    def get_price(sym, base, amount):
        try:
            base_key = exchanges[base.lower()]
        except KeyError:
            raise APIException(f"Валюта {base} не найдена!")

        try:
            sym_key = exchanges[sym.lower()]
        except KeyError:
            raise APIException(f"Валюта {sym} не найдена!")

        if base_key == sym_key:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}!')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}!')

        payload = {}
        headers = {
            "apikey": "2SzGt0EQVosrZfgFkI70CHyt2EVRG7xb"
        }

        r = requests.get(
            f"https://api.apilayer.com/exchangerates_data/convert?to={base_key}&from={sym_key}&amount={amount}",
            headers=headers, data=payload)
        resp = json.loads(r.content)
        new_price = resp['result']
        return new_price
