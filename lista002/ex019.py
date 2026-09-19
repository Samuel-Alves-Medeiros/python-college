senhas:list[str] = ["P", "N", "P", "P", "N", "P", "N", "N", "P", "N"]
preferencial:list[str] = []
normal:list[str] = []
contador_preferencial:int = 0
contador_normal:int = 0

for senha in senhas:
    if senha == "P":
        preferencial.append(senha)
        contador_preferencial+=1
    else:
        normal.append(senha)
        contador_normal +=1


print(f'Existem {contador_normal} senhas normais e {contador_preferencial} senhas preferênciais')
