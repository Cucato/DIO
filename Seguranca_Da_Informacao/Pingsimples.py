import os #importar o nodulo ou biblioteca os 

print("#" * 99)

ip_ou_host = input("Digite o Ip ou host a ser verificado: ")
print("_" * 99)
os.system('ping -n 6 {}'.format(ip_ou_host))
print("-" * 99)
