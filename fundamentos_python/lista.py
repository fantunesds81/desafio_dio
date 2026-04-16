try:
    lista1 = input().split()
    lista2 = input().split()
    
    # Convertendo para inteiros
    set1 = set(map(int, lista1))
    set2 = set(map(int, lista2))
    
    # Encontrando elementos comuns
    comuns = sorted(list(set1 & set2))
    
    print(f"Elementos comuns às duas listas: {comuns}")
    
except:
    print("Entrada inválida.")