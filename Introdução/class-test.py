class Aluno:
    def __init__(self,nome:str ,idade: int, matricula:int) -> None:

        self.nome = nome
        self.idade = idade
        self.matricula = matricula

nome_input:str = input('Nome: ')

idade_input:int = int(input('Idade: '))

matricula_input:int = int(input('Matricula: '))

aluno1 = Aluno(nome_input, idade_input, matricula_input)

print(aluno1.nome)