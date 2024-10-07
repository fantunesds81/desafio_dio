import itertools

string = input("String a ser permutada: ")

resuldado = itertools.permutations(string, len(string))

for i in resuldado:
    print(''.join(i))