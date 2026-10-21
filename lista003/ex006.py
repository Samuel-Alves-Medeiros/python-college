contato1 = {"nome": "Julia", "telefone": "81999990000", "favorito": True}
contato2 = {"nome": "Renato", "telefone": "81988887777"}

#Nesse for a variável temporaria 'contato' é referente ao dicionario, contato == dict
for contato in [contato1, contato2]:
    if contato.get('favorito'):
        print(contato)
