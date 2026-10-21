# nome: str = input('informe seu nome ')

usuario: dict = {
    'nome': 'piripapo',
    'idade': 19,
    'matricula': 123456789,
    'altura': 1.98,
    'endereco': {
        'rua': 'rua 1',
        'numero': 12,
        'cidade': 'cidade 1',
        'estado': 'pe',

    }

}

# for chave in usuario:
#     print(chave)

# retorna chave e valor
for k, v in usuario.items():
    print(f'a chave é {k} e o valor é {v}')

del usuario['altura']

usuario['nome'] = 'marcos'
usuario['jogo_fav'] = 'eldenring'
usuario['endereco']['cep'] = 55151625

print(usuario['nome'])
print(usuario['jogo_fav'])
print(usuario['endereco']['cep'])
print(usuario.get('endereco').get('cep'))

