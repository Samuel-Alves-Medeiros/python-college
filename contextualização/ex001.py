# (Questão 1) Desconsiderando a distância percorrida pela Artemis II no sobrevoo ao redor da lua,
# implemente um algoritmo que calcula a velocidade média do módulo Artemis II para ir e voltar da lua.
# Considere: Vm = S_total / T_total

S_TOTAL:int = 380000*2
T_TOTAL:int = 231

velocidade_media:float = S_TOTAL/T_TOTAL

print(f'A velocidade média do módulo Artemis II é de {velocidade_media}Km/h')