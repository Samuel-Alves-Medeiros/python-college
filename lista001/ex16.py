idade:int = int(input('Digite sua idade:'))
renda: float = float(input('Digite sua renda mensal'))
restricao:str = input('Você tem alguma restrição? (sim/não)')

tem_restricao:bool = restricao == 'sim'

if tem_restricao:
    print('sai daqui zé liseira')
elif idade >=18 and renda >=1500:
    print('Você pode solicitar um cartão de crédito')