usuarios = []

def cadastrar():
    usuario = {
        "email": input('Digite Seu e-mail'),
        "senha": input('Digite sua senha')
    }
    usuarios.append(usuario['email'])
    usuarios.append(usuario['senha'])

