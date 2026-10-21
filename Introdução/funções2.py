# def eh_par(numeros:list[int]) -> bool:
#     for numero in numeros:
#         if numero % 2 == 0:
#             return True

# print(eh_par([1,3,6,8]))

def opcao() -> bool:
    opc = input('Deseja parar? (s|n)').lower()
    if opc == 's':
        return True
    else: 
        return False
    

def dados() -> dict:

    nome:str = input('Digite seu nome: ')   
    cpf:str = input('Digite seu cpf: ')
    idade:int = int(input('Digite sua idade: '))
    peso:float = float(input('Digite seu peso: '))
    altura:float = float(input('Digite sua altura: '))

    imc = peso/altura**2

    dados_usuario:dict = {
        'nome': nome,
        'cpf': cpf,
        'idade': idade,
        'peso': peso,
        'altura': altura,
        'imc': imc
    }
    
    return dados_usuario

while True:
    resposta = opcao()
    if resposta:
        break
    else:
        usuario:dict = dados()

    