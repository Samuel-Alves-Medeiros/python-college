tempos:list[int] = [120, 340, 90, 500, 210, 175, 430, 60, 280, 340]
maior:int = tempos[0]
menor: int = tempos[0]

posicao_maior: int = 0
posicao_menor:int =0

for i in range(len(tempos)):
    if tempos[i] > maior:
        maior = tempos[i]
        posicao_maior = i
    if tempos[i] < menor:
        menor = tempos[i]
        posicao_menor = i

print(f'O maior tempo de resposta foi {maior} e sua posição na lista é {posicao_maior+1}')
print(f'O menor tempo de resposta foi {menor} e sua posição na lista é {posicao_menor+1} ')