lado1:int = int(input('Digite o primeiro lado do triângulo '))
lado2:int = int(input('Digite o segundo lado do triângulo '))
lado3:int = int(input('Digite o terceiro lado do triângulo '))

if lado1 > lado2 and lado1 > lado3:
    if lado1**2 == lado2**2 + lado3**2:
        print('verdadeiro')

elif lado2 > lado1 and lado2 > lado3:
    if lado2**2 == lado1**2 + lado3**2:
        print('verdadeiro')
    
elif lado3 > lado1 and lado3 > lado2:
    if lado3**2 == lado1**2 + lado2**2:
        print('verdadeiro')
    
else:
    print('falso')