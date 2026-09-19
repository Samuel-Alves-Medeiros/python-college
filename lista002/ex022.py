codigos_de_acesso:list[str] = ["A1", "B2","A1", "C3", "D4", "E5", "B2", "F6", "G7", "H8"]


for i in range(len(codigos_de_acesso)):
    for j in range(len(codigos_de_acesso)):
        if i != j:
            if codigos_de_acesso[i] == codigos_de_acesso[j]:
                print('true')
        
        