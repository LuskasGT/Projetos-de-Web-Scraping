import requests
from bs4 import BeautifulSoup
'''Aqui estamos pegando a cotação do dólar para real'''
link = "https://www.google.com/search?q=cotacao+dolar"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}

requisicao = requests.get(link, headers=headers)
site = BeautifulSoup(requisicao.text, "html.parser")



titulo = site.find("title")
print(titulo)

cotacao_dolar = site.find("span", class_="SwHCTb")
print(f'1 dolar é igual a {cotacao_dolar.get_text()}')
