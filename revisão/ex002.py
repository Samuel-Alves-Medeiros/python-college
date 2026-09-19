class Animal:
    def __init__(self, nome:str, especie:str, idade:str) -> None:
        self.nome = nome
        self.especie = especie
        self.idade = idade

gato = Animal('Jiji', 'Felinus', 9)

print(gato.nome, gato.idade, gato.especie)
