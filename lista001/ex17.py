lado1:int = int(input('Informe o valor do peimeiro lado '))
lado2:int = int(input('Informe o valor do segundo lado '))
lado3:int = int(input('Informe o valor do terceiro lado '))

if lado1 + lado2 < lado3 or lado2 + lado3 < lado1 or lado3 + lado1 < lado2:
    print('Esse triângulo é inválido')
else:
    if lado1 == lado2 ==lado3:
        print('Equilátero')
    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        print('Isóceles')
    else:
        print('Escaleno')