class Conta:
    def __init__(self, saldo=0):
        self._saldo = saldo

    def depositar(self, valor):
        pass

    def sacar(self, valor):
        pass



conta = Conta(100)
conta._saldo += 100
print(conta._saldo)
        