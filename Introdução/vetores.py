# for i in range(5):
#     idade: int = int(input('Idade:'))
#     if idade >18:
#         break


# Vetores: estruturas Homogêneas de Uma dimensão
# o tamanho de uma lista é a quantidade de elementos.
# a contagem do indice começa do 0
# Tamanho da lista != indice da lista

# idades: list[int] = []

# for _ in range (5):
#     idade: int = int(input('Digite sua idade'))
#     idades.append(idade)
# print(idades)

# idades: list[int] = [10,29,19,18,64]
# soma: int = 0 #acumulador
# for idade in idades:
#         soma+= idade
# print(soma)



# idades: list[int] = [10,29,19,18,64]
# soma: int = 0 #acumulador
# media: float = 0
# for idade in idades:
#         soma+= idade
# media = soma/ len(idades)
# print(media)


# notas:list[float] = [15.8, 13.4,14.5,11.0]
# soma:float = 0
# media: float = 0

# for nota in notas:
#     soma+=nota

# media = soma/len(notas) #A média é a soma das notas / pelo tamanho da lista

# print(media)

idades: list[int] = [10,29,19,18,64, 9]
menor: int = idades[0]
maior: int = idades[0]
for idade in idades:
    if idade < menor:
        menor = idade
    if idade > maior:
        maior = idade

print(f'o menor valor é {menor}  e o maior valor é {maior}')