import requests
res=requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL")
print(res)
res_json=res.json()
print(res_json)
cotacao_dolar=float(res_json["USDBRL"]["bid"])
print(cotacao_dolar)
cotacao_euro=float(res_json["EURBRL"]["bid"])
print("cotação do euro:",cotacao_euro)
print("========================conversão brl para usd============================")
brl=float(input("Digite um valor:"))
usd=brl/cotacao_dolar
print(f"Esse é o valor em dolar:{usd}")
print("========================conversão brl para euro============================")
brl=float(input("Digite um valor:"))
euro=brl/cotacao_euro
print(f"Esse é o valor em dolar:{euro}")

