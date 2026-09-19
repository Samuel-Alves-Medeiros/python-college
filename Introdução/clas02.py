class Company:

    def __init__(self, nome:str, cnpj:int, endereco:str, dono:str ) -> None:

        self.nome = nome
        self.cnpj = cnpj
        self.endereco = endereco
        self.dono = dono


apple = Company('apple', 40028922, 'rua luiz inácio bolsonaro da silva', 'donald j. musk' )

print(apple.nome, apple.cnpj, apple.endereco, apple.dono )