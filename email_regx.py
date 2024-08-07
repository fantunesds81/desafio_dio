import re # importando o modulo

# função principal
def valida_email(email):
    padrao = r'^[\w\.-]+@[\w\,-]+.\.\w+$'
    return re.match(padrao, email) is not None


endereco_email = input('Digite seu email: ')
resultado = valida_email(endereco_email)

if resultado == True:
    print(f'O Email: {endereco_email}, é válido')
else:
    print(f'O Email {endereco_email}, é Inválido.\n Informar o email correto')

