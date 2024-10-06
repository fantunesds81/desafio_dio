from cryptography.fernet import Fernet

# Gera uma chave e a salva em um arquivo
key = Fernet.generate_key()
with open("chave.key", "wb") as chave_arquivo:
    chave_arquivo.write(key)

# Carrega a chave
with open("chave.key", "rb") as chave_arquivo:
    key = chave_arquivo.read()

# Inicializa o objeto Fernet
fernet = Fernet(key)

# Lê o arquivo a ser criptografado
with open("arquivo.txt", "rb") as arquivo:
    arquivo_dados = arquivo.read()

# Criptografa os dados
arquivo_criptografado = fernet.encrypt(arquivo_dados)

# Salva os dados criptografados em um novo arquivo
with open("arquivo_criptografado.txt", "wb") as arquivo:
    arquivo.write(arquivo_criptografado)
