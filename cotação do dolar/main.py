import requests
from bs4 import BeautifulSoup as bs

url = "https://www.google.com/search?q=cotacao+dolar"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}


requisicao = requests.get(url, headers=headers)

site = bs(requisicao.text, "html.parser")


titulo = site.find('title')
print (titulo)

pesquisa2 = site.find("input", class_="gLFyf")
print(pesquisa2)