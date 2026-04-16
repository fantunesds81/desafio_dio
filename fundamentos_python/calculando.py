class Calculadora:
    def somar(self, a, b):
        return a + b


# Entrada de dados
num1 = int(input())
num2 = int(input())

# Criando objeto da classe
calc = Calculadora()

# Saída
resultado = calc.somar(num1, num2)
print(resultado)