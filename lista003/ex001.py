cadastro:dict = {"usuario": "ana123", "senha": "abc456"}

print('Digite seu usuário e senha\n')
      
usuario_input:str = input('Digite seu usuário ')
senha_input:str = input('Digite sua senha ')

if usuario_input == cadastro['usuario'] and senha_input == cadastro['senha']:
    print('Login efetuado com sucesso!')
else:
    print('Tentativa de login inválida. Verifique as informações e tente novamente.')