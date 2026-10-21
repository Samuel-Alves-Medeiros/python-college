livro:dict = {"titulo": "Duna", "autor": "Frank Herbert", "ano": 1965, "emprestado": False}

emprestimo:str = input('Você deseja pegar o livro emprestado? (sim|não)')

if emprestimo == 'sim':
    livro["emprestado"] = True
else:
    livro["emprestado"] = False

if emprestimo == 'sim':
    devolução:str = input('Deseja devolver o livro?(sim|não)')
    livro['emprestado'] = False if devolução == 'sim' else livro['emprestado'] == livro['emprestado']

for k,v in livro.items():
    print([k,v])