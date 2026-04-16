def contar_caracteres(string):
    contador = {}
    
    for caractere in string:
        if caractere in contador:
            contador[caractere] += 1
        else:
            contador[caractere] = 1
            
    return contador

texto = input()
resultado = contar_caracteres(texto)

print(resultado)