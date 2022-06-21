import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #objeto de conxao "s"

print('Cliente Socket criado com sucesso!!!')

host = 'localhost'
porta = 5433
menssagem = 'ola servidor firmeza?'

try:
    print('Cliente :' + menssagem)
    s.sendto(menssagem.encode(), (host, 5432))#pego a menssagem, empacoto e envio

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode() #desenpacotar os dados
    print('Cliente: ' + dados)
finally:
    print('Cliente: Fechando a Conexão')
    s.close()
