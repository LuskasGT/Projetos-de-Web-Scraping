import requests
from bs4 import BeautifulSoup as Bs

''' Aqui vou etsra fazendo a raspagem de uma foto de perfil de um usuário do github, vc escolhe quem é 
    Apenas relembrando como programa em .py com projeotos
'''

github = input("Diga-me qual usuário você deseja ver a foto de perfil: ")
url = f"https://github.com/{github}"

try:
    r = requests.get(url)
    soup = Bs(r.content, 'html.parser')
    avatar = soup.find('img', {'class': 'avatar-user'})

    if avatar is None:
        print("Usuário não encontrado, verifique se digitou correamente")
    else:
        print(avatar)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
