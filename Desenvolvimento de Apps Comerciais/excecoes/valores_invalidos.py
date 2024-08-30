# coding: utf-8
# author: fantunes

def input_float(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Número Inválido.")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

try:
    print(num1 / num2)
except ZeroDivisionError:
    print("Não é possivel dividir um número por zero!!!")
