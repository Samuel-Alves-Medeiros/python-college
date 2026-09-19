numero_lido:int = int(input('Digite um número inteiro qualquer'))
resto_divisao:int = numero_lido%2

print(f'O número é impar' if resto_divisao != 0 else 'O número é par')

# if resto_divisao != 0:
#     print(f'O número {numero_lido} é impar')
# else:
#     print(f'O número {numero_lido} é par')