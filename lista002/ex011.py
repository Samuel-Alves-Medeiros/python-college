consumo_semanal:list[int] = [320, 480, 610, 200, 550, 700, 150]
contador: int = 0

for megabites in consumo_semanal:
    if megabites > 500:
        contador+=1

print(f'em {contador} dias o consumo ultrapassou os 500 MB')