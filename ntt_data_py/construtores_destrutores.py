class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print('inicializando a classe...')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print('removendo a instancia da classe')

    def falar(self):
        print('auauauaua')


c = Cachorro('Chapie', "caramelo")
c.falar() 
        