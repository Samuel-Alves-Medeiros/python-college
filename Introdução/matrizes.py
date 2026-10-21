# Matriz => Lista com outras listas

m:  list[list[int]] = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


maior_valor:float = [0][0]
l:int = 0
c:int = 0

for i in range(len(m)):
    for j in range(len(m)):
        if m[i][j] > maior_valor:
            maior_valor = m[i][j]
            l = i
            c = j

print(f'O maior valor é {maior_valor} na linha {l} e na coluna {j}')
# new_list  = []
# for i in range(len(m)):
#     soma_linha = 0   
#     for j in range(len(m)):
#         soma_linha+= m[i][j]
#     new_list.append(soma_linha)

# print(new_list)

# for linha in m:
#     for coluna in linha:
#         print(coluna)

# m [1][1] = 10

# print(m)



