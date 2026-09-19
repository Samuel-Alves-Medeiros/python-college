#Match case 
#opcao:str = input('escolha uma opção ')

#match opcao:
#    case 'cadastrar'|'cadastro':
#        print('cadastrando....')
#    case 'editar':
#        print('editando')
#    case _: 
#        print('esse menu não existe')

#é possível criar uma variavel no match case

letra:str =  input('Escolha uma letra ')

match letra:
    case 'a'|'e'|'i'|'o'|'u':
        print('vogal')
    case _:
        print('consoante')