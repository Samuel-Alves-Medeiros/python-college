codigos:list[int] = [200, 404, 200, 500, 200, 404,200, 500, 404, 200]
contador_200:int = 0
contador_404:int = 0
contador_500:int = 0

for codigo in codigos: 
    if codigo == 200:
        contador_200+=1
    if codigo == 404:
        contador_404+=1
    if codigo == 500:
        contador_500 +=1

print(f'Existem {contador_200} codigos 200, {contador_404} codigos 404 e {contador_500} em códigos 500')