tarefas_tempo:list[int] = [15, 22, 8, 30, 12, 5, 18, 25, 10, 20]
contador:int = 0
soma:int = 0

for tempo in tarefas_tempo:
    contador+=1
    soma+= tempo 
    if soma >60:
        print(f'o tempo gasto é de {soma}, o total de tentativas necessárias para atingir esse tempo foram de: {contador}')
        break