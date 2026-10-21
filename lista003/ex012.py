assentos: list[list[bool]] = [
[True, True, False, True],
[False, False, True, True],
[True, False, False, False],
[True, True, True, False]
]

assentos_vazios:int = 0

for i in range(len(assentos)):
    for j in range(len(assentos)):
        if assentos[i][j] == False:
            assentos_vazios+=1
print(f'No total existem {assentos_vazios} assentos vazios')

# for linha in assentos:
#     for coluna in linha:
#         print(coluna) --> outra forma de solucionar o problema