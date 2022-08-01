import ipaddress

ip = '192.168.0.0/32'
#vao imprimir todas as redes da /0, poderia ser qualquer numero
rede = ipaddress.ip_network(ip,strict=False)
for ip in rede:
    print(ip)
