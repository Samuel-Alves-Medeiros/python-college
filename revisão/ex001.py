preco_produto:float = float(input('Digite o preço do produto, se não quiser mais adicionar digite 0 '))
contador:int = 0
acumulador:float = 0
maior_preco:float = 0
media_precos: float = 0

while preco_produto != 0:
    if preco_produto < 0:
        print('Preço inválido. Opreço deve ser maior que zero')
    else: 
        acumulador+= preco_produto
        contador+=1
        if preco_produto > maior_preco:
            maior_preco = preco_produto
    preco_produto:float = float(input('Digite o preço do produto, se não quiser mais adicionar digite 0 '))

if contador == 0:
    print('Nenhum produto foi adicionado. Impossível gerar saída.')
else:
    media_precos = acumulador/contador
    print(f'O total da compra é {acumulador}')
    print(f'A quantidade de produtos válidos é de {contador} produtos')
    print(f'O maior preço é R${maior_preco}')
    print(f'A média dos preços é R${media_precos}')
