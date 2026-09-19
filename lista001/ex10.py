nome:str = input('digite seu nome')
peso:float = float(input('Digite seu peso'))
altura:float = float(input('Digite sua altura'))
imc:float = peso/altura**2
if imc <18.5:
    print(f'{nome}, seu peso é {peso}, sua altura é {altura}, e seu IMC é {imc}. Você está abaixo do peso ideal')
elif imc >18.5 and imc <25:
    print(f'{nome}, seu peso é {peso}, sua altura é {altura}, e seu IMC é {imc}. Você está dentro do peso ideal')
elif imc >= 25 and imc <30:
    print(f'{nome}, seu peso é {peso}, sua altura é {altura}, e seu IMC é {imc}. Você está sobrepeso')
else:
    print(f'{nome}, seu peso é {peso}, sua altura é {altura}, e seu IMC é {imc}. Você está obeso')