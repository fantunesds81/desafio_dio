import hashlib

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

hash1 = hashlib.new('ripem160')
hash1.update(open(arquivo1, 'rb').read())

hash2 = hashlib.new('ripem160')
hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'O arquivo: {arquivo1} é diferente do arquivo: {arquivo2}')
else:
    print(f'O arquivo: {arquivo1} é igual do arquivo: {arquivo2}')

