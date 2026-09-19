salario: float = float(input('Qual é o seu salário? '))

reajuste_10: float = salario * 10/100
reajuste_7: float = salario * 7/100
reajuste_5: float = salario * 5/100

if salario <1500:
    print(f'Seu salário recebeu um reajuste de 10%, seu novo valor é de {salario + reajuste_10}')
elif salario >=1500 and salario < 3000:
    print(f'Seu salário recebeu um reajuste de 7%, seu novo valor é de {salario + reajuste_7}')
else:
    print(f'Seu salário recebeu um reajuste de 5%, seu novo valor é de {salario + reajuste_5}')
    