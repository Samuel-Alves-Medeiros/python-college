# status_servidor:list[bool] = [True, True, True, False, True, True, True, True, False, True, True, True, True, True, False]

# sequencia:int = 0
# maior_sequencia:int = 0 

# for status in status_servidor:
#     if status:  # if status: --> if status == True:// pois status já é um valor booleano 
#         sequencia += 1 
#         if sequencia > maior_sequencia:
#             maior_sequencia = sequencia
#     else:
#         sequencia = 0  
    
    

# print(f'A maior seqência cosecultiva de checagens "online" é de {maior_sequencia}  ')

def soma (a,b):
    if not isinstance(a, int) or not isinstance(b,int) :
        raise ValueError('Os números somados precisam ser inteiros')
    else:
        return a+b 

print(soma(29,8))


# i =1    

# resultado = int(input())

# match resultado:

#     case 1 | 2:
#         print('Olá')

#     case _:
#         print('Digite 1 ou 2')







                 