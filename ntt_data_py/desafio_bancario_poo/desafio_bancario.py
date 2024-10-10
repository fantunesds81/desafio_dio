from abc import ABC, abstractmethod
from datetime import datetime

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor
        self.data = datetime.now()

    def registrar(self, conta):
        conta._saldo -= self.valor
        conta._historico.append(f"Saque de {self.valor} em {self.data}")

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor
        self.data = datetime.now()

    def registrar(self, conta):
        conta._saldo += self.valor
        conta._historico.append(f"Depósito de {self.valor} em {self.data}")

class Conta(ABC):
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self._saldo = 0
        self._historico = []

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass

    def extrato(self):
        print(f"Extrato da conta {self.numero} - Titular: {self.titular}")
        for transacao in self._historico:
            print(transacao)
        print(f"Saldo atual: {self._saldo}")

class ContaCorrente(Conta):
    def __init__(self, numero, titular, limite):
        super().__init__(numero, titular)
        self.limite = limite

    def sacar(self, valor):
        if self._saldo + self.limite >= valor:
            saque = Saque(valor)
            saque.registrar(self)
            print(f"Saque de {valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente.")

    def depositar(self, valor):
        deposito = Deposito(valor)
        deposito.registrar(self)
        print(f"Depósito de {valor} realizado com sucesso.")

# Exemplo de uso
conta1 = ContaCorrente("12345", "Alice", 1000)
conta1.depositar(500)
conta1.sacar(200)
conta1.extrato()
