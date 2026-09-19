idades:list[int] =  [17, 22, 15, 30, 45, 16, 19, 60, 14, 25]
maior_de_idade:int = 0
menor_de_idade:int = 0

for idade in idades:
    if idade >=18:
        maior_de_idade+=1
    else:
        menor_de_idade+=1
print(f'Existem {maior_de_idade} maiores de idade na lista e {menor_de_idade} menores de idade.')