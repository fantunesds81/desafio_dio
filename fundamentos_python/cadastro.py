class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"


# Entrada de dados
nome = input()
idade = int(input())

# Criando objeto
pessoa = Pessoa(nome, idade)

# Saída
print(pessoa.apresentar())