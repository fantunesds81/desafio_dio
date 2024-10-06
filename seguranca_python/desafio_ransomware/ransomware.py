import os
import pyaes

# abrir o arquivo criptografado
file_name = 'teste.txt.ransomwaretroll'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

# chave de descriptografia

key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCBC(key)
descrypt_data = aes.decrypt(file_data)

# remove o arquivo descriptografado

os.remove(file_name)

#criar um novo arquivo descriptografado

new_file = 'teste.txt'
new_file = open(f'{new_file}','wb')
new_file.write(descrypt_data)
new_file.close()