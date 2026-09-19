# divisível por 4 mas
# em anos multuplos de 100 que não são multiplos de 400, não é bissxesto.
ano:int = int(input('Digite um ano e descubra se ele é bissexto ou não'))
calculo_ano_bissexto_4:int = ano%4
calculo_ano_bissexto_100:int = ano%100
calculo_ano_bissexto_400:int = ano%400

if calculo_ano_bissexto_4 == 0 and calculo_ano_bissexto_100 != 0:
    print('o ano é bissexto')
elif calculo_ano_bissexto_400 == 0:
    print('o ano é bissxesto')
else:
    print('o ano não é bissexto')
