contador:int = 0
numero:int = int(input('digite um número qualquer e veja sua tabuada de x '))

while contador <=10: 
    print(f'{contador} X {numero} = {contador * numero}')
    contador+=1
continuar:str = input('deseja continuar?')
