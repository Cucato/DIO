import itertools

string = input('String a ser permutada')
#resultado = itertools.permutations('abcdef', 6) #soma as possibilidades de 'abcdef com 6 digitos
resultado = itertools.permutations(string, len(string))
for i in resultado:
    print(''.join(i))
