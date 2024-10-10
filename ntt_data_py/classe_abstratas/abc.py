from abc import ABC, abstractmethod


class contoleRemoto(ABC):
    @abstractmethod
    
    
    def ligar(self):
        pass

    def desligar(self):
        pass

        
    @property
    def marca(self):
        return "Samsung"



class ControleTV(contoleRemoto):
    def ligar(self):
        print("Ligar a TV")

    def desligar(self):
        print("desligar a TV...")
        print("Desligado!!")

class ControleArCondicionado(contoleRemoto):
    def ligar(self):
        print("Ligando o ar condicionado......")
        print("Ligado!!")

    @property
    def marca(self):
        return "LG"




controle = ControleTV()
print(controle.marca)
controle.ligar()
controle.desligar()


controle = ControleArCondicionado()
controle.ligar()
print(controle.marca)

