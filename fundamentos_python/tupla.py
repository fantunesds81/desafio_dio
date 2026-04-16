entrada = input()

# Convertendo a entrada em tupla de inteiros
elementos = tuple(map(int, entrada.split()))

# Calculando a soma
soma = sum(elementos)

# Saída no formato correto
print(f"A soma dos elementos da tupla é: {soma}")