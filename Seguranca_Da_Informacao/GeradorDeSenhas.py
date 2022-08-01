#https://md5decrypt.net/en/   codifica e descodifica palavras

import random, string

tamanho = int(input('Entre com um numero')) #tamanhao da senha

chars = string.ascii_letters + string.digits + '¹²³£¢¬!@#$%¨&*()_+'
# o primeiro é pra senhas com letras maiusculas e minusculas
# o segundo é para numeros
# o terceiro para esses simbolos serem adicionados

rnd = random.SystemRandom() # ela utilisa de outra biblioteca chamada os.urandon
# #ela rejanumeros aleatórios atraves de uma base fornecida

print(''.join(rnd.choice(chars) for i in range(tamanho)))
#join é junção
