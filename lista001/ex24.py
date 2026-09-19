idade:int = int(input('Qual é a sua idade?'))
pcd:str = input('é pcd? (sim | não)')
respostas_positivas:str = ['sim', 'sou', 'yeah, baby']
horas_estaciodanas:int = int(input('ha quantas horas seu veículo está estacionado?'))

if idade <60 and pcd not in respostas_positivas:
    print('Vaga restrita, acesso não liberado')
else:
    if horas_estaciodanas >2:
        print('Você excedeu o tempo limite da vaga')
    else:
        print('Acesso liberado')