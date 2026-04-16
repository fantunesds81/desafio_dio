class ConversorTemperatura:
    def celsius_para_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32


# Entrada de dados
celsius = float(input())

# Criando objeto
conversor = ConversorTemperatura()

# Convertendo e exibindo resultado
fahrenheit = conversor.celsius_para_fahrenheit(celsius)
print(fahrenheit)