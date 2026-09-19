idade:int = int(input('Digite sua idade '))
peso:float = float(input('Digite seu peso em kg '))
altura:float = float(input('Digite sua altura em M '))
imc:float = peso/altura**2

print('calculo não aplicavel para crianças' if idade<12 else f'seu IMC é {imc}') 