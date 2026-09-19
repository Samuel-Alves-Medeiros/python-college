idade:int = int(input('Digite sua idade e descubra se seu voto é obrigatório: '))

if idade >=16 and idade <18 or idade >=70:
    print('Voto facultativo')
elif idade >=18 and idade <70:
    print('Voto obrigatório')
else:
    print('Não vota')