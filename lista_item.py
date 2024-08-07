def cadastrar_itens():
    # Definindo uma lista inicial de 3 itens
    itens = []
    
    # Solicitando ao usuário cadastrar os 3 itens
    print("Cadastro de Itens:")
    for i in range(3):
        item = input(f"Digite o {i+1}º item: ")
        itens.append(item)
    
    return itens

def exibir_itens(itens):
    # Exibindo a lista de itens cadastrados
    print("\nLista de Itens:")
    for i, item in enumerate(itens, 1):
        print(f"{i}. {item}")

# Função principal para gerenciar o cadastro e exibição dos itens
def main():
    # Cadastro dos itens
    lista_itens = cadastrar_itens()
    
    # Exibição dos itens cadastrados
    exibir_itens(lista_itens)

# Executar o programa
if __name__ == "__main__":
    main()
