import hashlib

arquivo1 = 'ComparadorA'
arquivo2 = 'ComparadorB'

hash1 = hashlib.new('ripemd160')

hash1.update(open(arquivo1, 'rb').read()) # .update compara o hash
# r=abre para leitura
# w = abra para escrita
# x = abra para criação exclusiva
# a = abre para escrita no final
# b = bianrio
# t = modo de texto
# + = abreto para atualisação (leitura e escrita)
hash2 = hashlib.new('ripemd160')

hash2.update(open(arquivo2, 'rb').read())

if hash1 .digest() != hash2.digest():
    print(f'O arquivo:{arquivo1} é diferente do arquivo:{arquivo2}')# esse f' é outra maneira de utilizar o .format
    print('O hash do arquivo Comparador1 é : ',hash1.hexdigest())
    print('O hash do arquivo Comparador2 é : ', hash2.hexdigest())
    # o .hexdigest codifica em hexadecimal
else:
    print(f'O arquivo:{arquivo1} é igual o arquivo:{arquivo2}')
    print('O hash do arquivo Comparador1 é : ', hash1.hexdigest())
    print('O hash do arquivo Comparador2 é : ', hash2.hexdigest())
# o texto foi tranformado em md5 e deoius em hexadecimal
