nota1:float = float(input('Digite a primeira nota '))
nota2:float = float(input('Digite a segunda nota'))
media:float = (nota1 + nota2) /2
if  media >= 7:
    print('Aprovado')
elif media >=5 and media<7:
    print('recuperação')
else:
    print('reprovado')