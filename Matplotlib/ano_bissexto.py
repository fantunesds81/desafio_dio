def verificar_bissexto(ano):
    # Verifica se o ano é divisível por 4
    if ano % 4 == 0:
        # Verifica se o ano é divisível por 100
        if ano % 100 == 0:
            # Se for divisível por 100, deve ser divisível por 400
            if ano % 400 == 0:
                return "Sim"
            else:
                return "Não"
        else:
            return "Sim"
    else:
        return "Não"

# Exemplo de uso:
ano = int(input("Digite um ano: "))
resultado = verificar_bissexto(ano)
print("O ano", ano, "é bissexto?", resultado)
