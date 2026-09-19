tamanhos:list[int] = [50, 120, 30, 90, 200, 15, 60, 180, 45, 75]
soma_exta:int = 165

for i in range (len(tamanhos)-1):

    soma = tamanhos[i] + tamanhos [i+1]

    if soma == soma_exta:
        print(f'A soma dos arquivos de tamanho {tamanhos [i]} + {tamanhos[i+1]} é exatamente {soma}')
    else: 
        print('não existe nenhum par de arquivos cuja soma seja exatamente 165')
