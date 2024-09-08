class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula


    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"
     
def mostrar_valores(*obj):
    for obj in obj:
        print(obj)


aluno_1 = Estudante("fabio", 1)
aluno_2 = Estudante("antunes", 2)

mostrar_valores(aluno_1, aluno_2)
print("="*125)
aluno_1.matricula = 3
mostrar_valores(aluno_1, aluno_2)
        