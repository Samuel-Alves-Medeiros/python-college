config:dict = {"dificuldade": "normal", "som": "ativado", "legendas": "desativado"}

while True:
    print('CONFIGURAÇÕES\n')
    print('1 - Dificuldade')
    print('2 - Som')
    print('3 - Legendas')
    print('4 - Sair\n')

    opcao_mod:str = input('Selecione uma das opções para modificar (1,2,3) ou (4) para sair\n ')

    if opcao_mod == '4':
        break
    else:
        match opcao_mod:
            case '1':
                print('Escolha uma dificuldade entre (Fácil, Normal e Difícil)')
                config_dificuldade:str = input('').lower()
                match config_dificuldade:
                    case 'fácil'|'facil':
                        config['dificuldade'] = 'fácil'
                        print('Dificuldade modificada com sucesso!')
                        input('Aperte "Enter" para proseguir')
                    case 'normal':
                        config['dificuldade'] = 'normal'
                        print('Dificuldade alterada com sucesso!')
                        input('Aperte "Enter" para proseguir')
                    case 'difícil'|'dificil':
                        config['dificuldade'] = 'difícil'
                        print('Dificuldade alterada com sucesso!')
                        input('Aperte "Enter" para proseguir')
                    case _:
                        print('ERRO: Digitação errada')
                        print('Escreve o negócio certo, seu animal!')
                        input('Aperte "Enter" para proseguir')
            case '2':
                print('Você deseja deixar o som ativado ou desativado?')
                config_som:str = input('').lower()
                match config_som:
                    case 'ativado':
                        config['som'] = 'ativado'
                        print('Som alterado com sucesso [Ativado]')
                        input('Aperte "Enter" para proseguir')
                    case 'desativado':
                        config['som'] = 'desativado'
                        print('Som alterado com sucesso [Desativado]')
                        input('Aperte "Enter" para proseguir')
                    case _:
                        print('ERRO: Digitação errada')
                        print('Escreve o negócio certo, seu animal!')
                        input('Aperte "Enter" para proseguir')
            case '3':
                print('Você deseja deixar as legendas ativadas ou desativadas?')
                config_legendas:str = input('').lower()
                match config_legendas:
                    case 'ativada' | 'ativado'| 'ativadas':
                        config['legendas'] = 'ativado'
                        print('Legendas alteradas com sucesso [Ativado]')
                        input('Aperte "Enter" para proseguir')
                    case  'desativada' | 'desativado' | 'desativadas':
                        config['legendas'] = 'desativado'
                        print('Legendas alteradas com sucesso [Desativado]')
                        input('Aperte "Enter" para proseguir')
                    case _:
                        print('ERRO: Digitação errada')
                        print('Escreve o negócio certo, seu animal!')
                        input('Aperte "Enter" para proseguir')

for k,v in config.items():
    print([k,v])

