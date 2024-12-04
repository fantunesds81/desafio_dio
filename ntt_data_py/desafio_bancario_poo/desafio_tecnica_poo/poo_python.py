class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

class Relatorio:
    def __init__(self):
        self.vendas = []

    def adicionar_venda(self, venda):
      if isinstance(venda, venda):
        self.vendas.append(venda)
      else:
        raise TypeError("o objeto não é uma instância da classe venda")
      
        # TODOS: Verifique se o objeto passado é uma instância da classe Venda.
        # Isso ajuda a garantir que apenas vendas válidas sejam adicionadas ao relatório.
        

    def calcular_total_vendas(self):
        total = 0
        for venda in self.vendas:
          total += venda.quantidade * venda.valor
          
            # TODOS: Calcule o total de vendas baseado nas vendas adicionadas:
             # O cálculo deve multiplicar a quantidade pelo valor de cada venda e somar ao total.
            
        return total


def main():
    relatorio = Relatorio()
    
    for i in range(3):
        produto = input()
        quantidade = int(input())
        valor = float(input())
        venda = Venda(produto, quantidade, valor)
        relatorio.adicionar_venda(venda)
    
    # TODOS: Exiba o total de vendas usando o método calcular_total_vendas.
    # Utilize o método `calcular_total_vendas` da classe `Relatorio` para mostrar o total acumulado das vendas.
    total_vendas = relatorio.calcular_total_vendas()
    print(f"Total de vendas: {total_vendas:.2f}")


if __name__ == "__main__":
    main()