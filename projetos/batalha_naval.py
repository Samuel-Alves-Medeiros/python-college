from random import randint


bombs = []

for i in range(4):
    x,y = [randint (0,4) for _ in range(2)]
    bombs.append((x,y))

bomba = '💣'
agua = '🌊'

tabuleiro = [
    ['🟦', '🟦', '🟦', '🟦', '🟦'],
    ['🟦', '🟦', '🟦', '🟦', '🟦'],
    ['🟦', '🟦', '🟦', '🟦', '🟦'],
    ['🟦', '🟦', '🟦', '🟦', '🟦'],
    ['🟦', '🟦', '🟦', '🟦', '🟦']
]

for linha in tabuleiro:
    print(linha)

x:int = 0
y:int = 0

if x > 4 or y > 4:
    print('O número do x e do y devem ser menor ou igual a 4')

pontuacao_positiva:int = 0
pontuacao_negativa:int = 0
pontuacao_total = 0

limite_falhas:int = 4
contador_bombas:int = 0

cordenadas_usadas:list[int] = []

while True:
    encerrar_jogo = input('deseja encerrar o jogo? (s|n)')
    if encerrar_jogo == 's':
        print('Jogo encerrado... ')
        break
    else:
        x:int = int(input('Digite a cordenada x (linha)'))
        y:int = int(input('Digite a cordenada y (coluna)'))
        if (x,y) in cordenadas_usadas:
            print('cordenadas_usadas já usadas')
        else:
            cordenadas_usadas.append((x,y))
            if (x,y) in bombs:
                tabuleiro[x][y] = bomba
                pontuacao_negativa-=1
                contador_bombas+=1
                print(f'Caiu na bomba... Você tem {limite_falhas - contador_bombas} tentativas restantes.')
                print('-1 ponto')
                print(f'Pontuação total: {pontuacao_positiva + pontuacao_negativa}')
                if contador_bombas == 4:
                    print('Game Over!')
                    break
            else:
                tabuleiro[x][y] = agua
                pontuacao_positiva+=1
                print('Safe...')
                print('+1 ponto')
                print(f'Pontuação total: {pontuacao_positiva + pontuacao_negativa}')
            for linha in tabuleiro:
                print(linha)
