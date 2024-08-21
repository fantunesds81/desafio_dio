import hashlib

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

def calcular_hash(arquivo, algoritmo):
    """Calcula o hash de um arquivo usando o algoritmo especificado."""
    hash_obj = hashlib.new(algoritmo)
    try:
        with open(arquivo, 'rb') as f:
            while chunk := f.read(8192):
                hash_obj.update(chunk)
    except FileNotFoundError:
        print(f'Erro: O arquivo {arquivo} não foi encontrado.')
        return None
    except IOError as e:
        print(f'Erro ao ler o arquivo {arquivo}: {e}')
        return None
    return hash_obj.digest()

hash1 = calcular_hash(arquivo1, 'ripemd160')
hash2 = calcular_hash(arquivo2, 'ripemd160')

if hash1 is None or hash2 is None:
    # Se algum dos arquivos não puder ser lido, não podemos comparar.
    print('Não foi possível comparar os arquivos.')
elif hash1 != hash2:
    print(f'O arquivo: {arquivo1} é diferente do arquivo: {arquivo2}')
else:
    print(f'O arquivo: {arquivo1} é igual ao arquivo: {arquivo2}')
