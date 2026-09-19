senha:str = 'Pirip@po'
contador: int = 0 

while contador <3:
    contador+=1
    tentativa_senha: str = input('Digite sua senha.')
    if tentativa_senha == senha:
        print('Senha correta, acesso liberado')
    elif contador == 3 and tentativa_senha != senha:
        print('Sistema bloqueado.')
    else:
        print('Senha incorreta. Tente novamente.')
    