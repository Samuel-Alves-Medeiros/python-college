tabuleiro:list[list[str]] = [
["X", "X", "X"],
["O", "O", ""],
["O", "X", " "]
]

contador:int = 0
for linha in tabuleiro:
    print(linha)

for linha in tabuleiro:
    if linha[0] == linha[1] and linha[1] == linha[2]:
        print(f'Ganhou na linaha {contador}')
    else:
        print(f'Não ganhou na linha {contador}')
    contador+=1
        
