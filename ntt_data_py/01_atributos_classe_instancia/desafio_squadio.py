import sys

# Lista para armazenar os itens
itens = []

# Solicita os itens ao usuário
for i in range(3):
    print(f"Digite o nome do item {i+1}: ", end="")
    item = sys.stdin.readline().strip()
    itens.append(item)

# Exibe a lista de itens
print("\nLista de itens:")
for item in itens:
    print(f"- {item}")


'''

# Lista para armazenar os itens
itens = []

# Solicite os itens ao usuário
for i in range(3):
    item = sys.stdin.readline().strip()
    itens.append(item)

# Exibe a lista de itens
print("Lista de itens:")
for item in itens:
    print(f"- {item}")

'''