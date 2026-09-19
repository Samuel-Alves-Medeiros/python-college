notas: list [float] = [8.5, 6.0, 9.2, 4.5, 7.0, 5.5, 10.0, 3.8, 6.9, 7.5]
lista_aprovados:list[float] = []
lista_reprovados:list[float] = []

for nota in notas:
    if nota >=7:
        lista_aprovados.append(nota)
    else:
        lista_reprovados.append(nota)

print(f'Aprovados: {lista_aprovados}')
print(f'Reprovados: {lista_reprovados}')