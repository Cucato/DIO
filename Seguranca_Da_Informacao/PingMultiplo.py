import os
import time

with open('host.txt') as file:
    dump = file.read()
    dump = dump.splitlines() # coloca em linhas e nao em colunas

    for ip in dump:
        print('Verificando o ip: ', ip)
        print("-" * 99)
        os.system('ping -n 2 {}'.format(ip))
        print("-" * 99)
        time.sleep(5)
