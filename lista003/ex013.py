assentos: list[list[bool]] = [
[True, True, False, True],
[False, False, True, True],
[True, False, False, False],
[True, True, True, False]
]

linha:int = 0
coluna:int = 0
assentos_vazios:int = 0

for i in range(len(assentos)):
    linha+=1
    for j in range(len(assentos)):
        coluna+=1
        if assentos[i][j] == False:
            print(f'O assento na linha {linha} e coluna {coluna} é o primeiro vago')
            break
    if assentos[i][j] == False:
        break
