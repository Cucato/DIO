import ctypes
#para proteger os arquivos de uma pasta
atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW('Ocutar.txt', atributo_ocultar)

if retorno:
    print('Arquivo foi ocultado')
else:
    print('Arquivo não ocultado') 
