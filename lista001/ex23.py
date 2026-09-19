score:int = int(input('Digite seu score de cédito (0 a 1000)'))
idade:int = int(input('Digite sua idade'))
inadinplencia:str = input('você possui hoitórico de inadinplência? (sim | não)').lower()

inadinplencia_valor:bool = inadinplencia == 'sim'

if inadinplencia_valor == True:
    print('Risco alto (Cheirinho de caloteiro)')
else:
    if score >=700 and idade >=21:
        print('Risco baixo')
    else:
        print('Risco médio')