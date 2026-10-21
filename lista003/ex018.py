acessos:list[list[int]] = [
[2, 5, 3, 8, 1],
[0, 1, 2, 2, 0],
[4, 6, 5, 9, 3]
]

soma_de_salas:list[int] = []

for i in range(len(acessos)):
    soma = 0
    for j in range(len(acessos[i])):
        soma += acessos[i][j]
    soma_de_salas.append(soma)

mais_usada:int = 0

for sala in soma_de_salas:
    if sala > mais_usada:
        mais_usada += 1
coluna_horario:int = 0
soma_horarios:list[int] = []
soma = 0
lista_de_horios:list[int] = []

while True:
    for linha in acessos:
        soma_horarios.append(linha[coluna_horario])
        soma = 0
        for horario in soma_horarios:
            soma+= horario

    lista_de_horios.append(soma)


    coluna_horario+=1
    if coluna_horario == len(acessos[0]):
        break
    

    
        

print(f'A sala mais usada foi a sala {mais_usada}\n')
print(f'{soma_horarios}')
print(f'{lista_de_horios}')
