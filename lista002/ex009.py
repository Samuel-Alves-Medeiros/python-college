# senha_correta:str = 'admin123'
# tentativa_senha:str = input('Digite sua senha ')

# while tentativa_senha != senha_correta:
#     print('Senha Incorreta. Tente novamente.')
#     tentativa_senha:str = input('Digite sua senha ')

# print('Acesso liberado, a senha está correta. :)')


class Login:
    SENHA = 'piripapo'
    

senha_user = input('Digite sua senha: ')

if senha_user == Login.senha:
    print('senha correta')
