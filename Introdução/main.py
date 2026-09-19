#ICM calculator#
nome:str = input('Qual o seu nome?')
altura:float = float(input('Qual é a sua alturs em M'))
peso:float = float(input('qual é o seu peso em kg?'))
imc:float = peso/altura**2
print(f'Olá,{nome}! Seu peso é {peso}, sua altura é{altura} e seu IMC é {imc}')
