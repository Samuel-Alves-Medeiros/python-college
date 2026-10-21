temperaturas:list[list[float]] = [
[22.5, 24.0, 27.3, 25.1],
[21.0, 23.5, 26.8, 24.0],
[23.2, 25.5, 28.9, 26.3]
]

horario1:list[float] = []
horario2:list[float] = []
horario3:list[float] = []
horario4:list[float] = []

maior_temperatura:int = temperaturas[0][0]
area:int = 0
horario:int = 0

for i in range(len(temperaturas)):
    area+=1
    horario = 0
    for j in range(len(temperaturas)+1):
        horario+=1
        if temperaturas[i][j] > maior_temperatura:
            maior_temperatura = temperaturas[i][j]


for linha in temperaturas:
    horario1.append(linha[0])
    horario2.append(linha[1])
    horario3.append(linha[2])
    horario4.append(linha[3])

def media_horario (tempo):
    soma_horarios:float = 0
    for horario in tempo:
        soma_horarios += horario
    media:float = soma_horarios/len(tempo)
    return media



print(f'A maior temperatura foi de {maior_temperatura}º registrada na área {area} no horario {horario}')
print(f'A temperatura média do horario 1 é de {media_horario(horario1):.2f}')
print(f'A temperatura média do horario 2 é de {media_horario(horario2):.2f}')
print(f'A temperatura média do horario 3 é de {media_horario(horario3):.2f}')
print(f'A temperatura média do horario 4 é de {media_horario(horario4):.2f}')


