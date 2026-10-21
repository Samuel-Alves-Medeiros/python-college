# m = [
#     [0,0,0],
#     [1,1,1],
#     [2,2,2]
# ]

# def printar(m):
#     for linha in m:
#         print(linha)

# printar(m)

# def nome_funcao(a:int) -> int:
#     #processamento
#     return


# def media (n1, n2, div) -> float: 
#     return (n1 + n2)/div


# def sum(n1:int, n2:int):
#     resultado:int = n1 + n2
#     return resultado
# print(sum(4,5))

# def multiply(n1:int, n2:int) -> int:
#     resultado:int = n1 * n2
#     return resultado

# #Se uma dunção não retorna nada explicitamente ela retorna implicitamento o valor None
# def div(n1:int, n2:int) -> int:
#     if n2 != 0:
#         resultado = n1/n2
#         return resultado
#     else:
#         return ('Não dá pra dividir por zero')

# resultado_multy:int = multiply(12,4)
# print(resultado_multy)

# resultado_div:int = div(100,12)
# print(resultado_div)

# # _______________________________________________________________________________________________
# #Function sem retono e sem parâmetro:

# def ola(nome:str) -> None:
#     print(f'Olá {nome}\n')

# ola('Piripapo')

# Função que não retorna nada é um procedimento

# subtrair = lambda x,y: x-y

# print(subtrair(10, 5))

# def subtrair(x = 10, y = 10):
#     return x - y
m:list[list[str]] = [
["-", "-", "-"],
["-", "-", "-"],
["-", "-", "-"]
]

def imprimir_matriz(matriz) -> None:
    for linha in matriz:
        print(' '.join(linha))

def jogar(simbolo:str, c1:int, c2:int, m:list[list[str]]) ->None:
    m[c1][c2] = simbolo

def solicitar_dados() -> list:
    simbolo:str = input('Qual símbolo você quer jogar? ')
    c1:int = int(input('Digite a primeira cordenada '))
    c2:int = int(input('Digite a segunda cordenada '))
    return [simbolo, c1,c2]

while True:
    parar_jogo: int= int(input('Digite 1 para jogar e 0 para parar: '))
    if parar_jogo == 0:
        break

    imprimir_matriz(m)
    print('')
    s, l, c = solicitar_dados()
    jogar(s, l, c,  m)
    imprimir_matriz(m)