#  Self.nome = nome [Self.nome -> varáel da classe] [nome dps do igual -> parâmetro da classe]
#  a função inicial define o que é preciso para a classe existir.

class Aluno: 



    def __init__(self, nome:str, idade:int, piripapo:bool ) -> None:
        self.nome = nome
        self.idade = idade 
        self.piripapo = piripapo




aluno1 = Aluno('samuel', 852, True)

aluno2 = Aluno('Piripapo', 656, False)

print(aluno2.nome)

