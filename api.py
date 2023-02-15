import requests
import json

base_key = "USD"
sym_key = "RUB"
amount = 100


payload = {}
headers= {
  "apikey": "2SzGt0EQVosrZfgFkI70CHyt2EVRG7xb"
}

r = requests.get(f"https://api.apilayer.com/exchangerates_data/convert?to={base_key}&from={sym_key}&amount={amount}", headers=headers, data = payload)
resp = json.loads(r.content)
new_price = resp['result']

print(new_price)
