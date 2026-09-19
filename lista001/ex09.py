lado1:int = int(input('Digite o valor do primeiro lado do triângulo'))
lado2:int = int(input('Digite o valor do segundo lado do triângulo'))
lado3:int = int(input('Digite o valor do terceiro lado do triângulo'))

if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
    print('o triânulo é equilátero')
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print('o triângulo é isóceles')
else:
    print('o triângulo é escaleno')