temperaturas_do_dia:list[int] = [22, 24, 23, 25, 29, 31, 30, 28, 26, 24, 23, 22]

maior_variacao = 0 

for i in range(len(temperaturas_do_dia)-1):

    variacao = temperaturas_do_dia[i] - temperaturas_do_dia[i+1]
    if variacao <0:
        variacao = variacao * -1

    if variacao > maior_variacao:
        maior_variacao = variacao

print(maior_variacao)