from cryptography.fernet import Fernet

# Carrega a chave de criptografia
with open("chave.key", "rb") as chave_arquivo:
    key = chave_arquivo.read()

# Inicializa o objeto Fernet com a chave carregada
fernet = Fernet(key)

# Lê o arquivo criptografado
with open("arquivo_criptografado.txt", "rb") as arquivo:
    arquivo_criptografado = arquivo.read()

# Descriptografa os dados
arquivo_descriptografado = fernet.decrypt(arquivo_criptografado)

# Salva os dados descriptografados em um novo arquivo
with open("arquivo_descriptografado.txt", "wb") as arquivo:
    arquivo.write(arquivo_descriptografado)
