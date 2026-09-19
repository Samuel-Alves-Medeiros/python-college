valor_compra:float = float(input('qual o valor da sua compra?'))
tipo_cliente:str = input('você é cliente VIP ou comum? (vip|comum)')
desconto15:float = valor_compra*15/100
desconto5:float = valor_compra*5/100
if tipo_cliente == 'vip' and valor_compra >= 200:
    print(f'seu desconto é de {desconto15}, o prço total da sua compra é de {valor_compra - desconto15}')
elif tipo_cliente == 'comum' and valor_compra >=500:
    print(f'seu desconto é de {desconto5}, o valor total da sua compra é de {valor_compra - desconto5}')
else:
    print('não tem desconto')