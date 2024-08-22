class bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano 
        self.valor = valor

    def buzinar(self):
        print('plim plim')

    def parar(self):
        print('freando.....')
        print('parouuuuuuuu')

    def correr(self):
        print(" vrummmmmmmmmmmm")


b1 = bicicleta("vermelha", "caloi", 2024, 600)

b1.buzinar()
b1.correr()
b1.parar()



    
    


