imagem:list[list[int]] = [
[10, 20, 15, 5],
[200, 210, 195, 220],
[30, 25, 10, 15],
[180, 190, 205, 200]
]

soma_de_todos_os_valores:int = 0
tamanho_linha:int = len(imagem[0])
tamanho_imagem:int = len(imagem)

for linha in imagem:
    for coluna in linha:
        soma_de_todos_os_valores += coluna

tamanho_total = tamanho_imagem * tamanho_linha
media:float = soma_de_todos_os_valores/tamanho_total

if media < 128:
    print(f'A imagem tem o valor de {media} e é predominantemente escura')
else:
    print(f'A imagem tem o valor de {media} e é predominantemente clara')

