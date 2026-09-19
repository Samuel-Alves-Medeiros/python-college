tempo_de_resposta:list [int] = [120, 350, 90, 500, 210, 175, 430, 60, 280, 340]
contador:int = 0

for i in tempo_de_resposta:
    if i > 200:
        contador+=1
print(f'{contador} respostas ultrapassaram os 200 ms')
