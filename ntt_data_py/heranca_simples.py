class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    
    def ligar_motor(self):
        print('ligando o motor ')


class Motocicleta(Veiculo):
    pass



class Carro(Veiculo):
    pass



class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado 

    def esta_carregado(self):
        print(f"{'sim' if self.carregado else 'não'} estou carregado ")
    


moto = Motocicleta('preta','abc-123', 2)
moto.ligar_motor()

carro = Carro('white', 'xde-321', 4)
carro.ligar_motor()

caminhao = Caminhao('roxo', 'ctl-963', 10, True)
caminhao.ligar_motor()
caminhao.esta_carregado()