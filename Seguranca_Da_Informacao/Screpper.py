from bs4 import BeautifulSoup

import requests

site = requests.get('https://www.climatempo.com.br/').content # O .content pega todo conteudo e joga no site
#objeto site recebendo o conteudo da requisição http do site...
soup = BeautifulSoup(site, 'html.parser')
#objeto soup baixando do site o html
#print(soup.prettify()) #sem o "#" buscamos no site o html inteiro
#prettify tranforma html em string

Temperatura = soup.find('span', class_="-bold -gray-dark-2 -uppercase -font-12 _padding-5")
print(Temperatura.string)# buscamos no html no codigo expecivico e encontramos a frase ou palavra
#print(soup.title.string)
print(soup.p) #brinque neses ultimos 3
print(soup.find('admin'))#para encontar o administrador da pagina
