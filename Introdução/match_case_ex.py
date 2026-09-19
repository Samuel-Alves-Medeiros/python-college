
#Ex 01

# menu:int = int(input('Digite 1 para cadastrar, 2 para consultar e 3 para sair '))

# match menu:
#     case 1:
#         print('Cadastrando...')
#     case 2:
#         print('Consultando...')
#     case 3:
#         print('Saindo....')
#     case _:
#         print('Opção inválida. Digite 1,2 ou 3')

#Ex 02

#operacao:str = input('digite um operador numérico: + | - | * | /')

# match operacao:
#     case '+':
#         print('Soma')
#     case '-':
#         print('subtração')
#     case '*':
#         print('multiplicação')
#     case '/':
#         print('divisão')
#     case _:
#         print('Operador inválido')

#Ex 03

# dia_da_semana:str = input('Digite o dia da semana') 

# match dia_da_semana:
#     case 'sábado' | 'domingo':
#         print('Fim de semana')
#     case _:
#         print('Dia útil')

#Ex 04

mes_do_ano:int = int(input('Digite o número de um mês e descubra a qual trimestre ele pertence: '))

match mes_do_ano:
    case 1|2|3:
        print('Primeiro trimestre')
    case 4|5|6:
        print('Segundo trimestre')
    case 7|8|9:
        print('terceiro trimestre')
    case 10|11|12:
         print('Quarto trimestre')
    case _:
        print('Digite um número de 1 a 12')       