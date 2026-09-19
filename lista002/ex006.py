pares:list[int] = []

for i in range (1,31):
    if i %2 == 0:
        pares.append(i)
print(f'os números pares entre 1 e 30 são {pares}')