numeros:list[int] = []

numero_usuario:int = int(input('Digite quantos números quiser, caso não queira mais digitar, escreva -1 '))

while numero_usuario != -1:
    numeros.append(numero_usuario)
    numero_usuario:int = int(input('Digite quantos números quiser, caso não queira mais digitar, escreva -1 '))

print(numeros)