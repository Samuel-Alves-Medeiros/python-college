idade:int = int(input('Digite sua idade'))
cnh_suspensa:str = input('você tem a cnh suspensa?(sim|não)')
nota_exame:int = int(input('Qual foi a sua nota do exame?'))
cnh_valor:bool = cnh_suspensa == 'sim'

if idade >=18 and  not cnh_valor and nota_exame >=7:
    print('você pode emitir sua carteira')
elif idade <18:
    print('Você é menor de idade')
elif cnh_valor:
    print('Sua cnh está suspensa')
elif nota_exame <7:
    print('Nota baixa, burrão kkkkkk')

