import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #OBJETO DE CONnexao

print('Sockt criado com sucesso')

host = 'localhost'
port = 5432

s.bind((host,port)) #liga o cliente atravez do servidor e da porta
mensagem = '\nServidor: Oláaaaaa cliente, beleza??' #se der certo, o bind ficara como verdadeiro

while 1: #enquanto verdadeiro,ele vai receber 4096bits atravez do objeto de conexao, guardadndo dentro de endereço e de dados
    dados, end = s.recvfrom(4096)

    if dados:
        print('Servidor enviando mensagem ...')
        s.sendto(dados + (mensagem.encode()), end)
