precos = {"maçã": 2.50, "pão": 5.00, "leite": 4.80, "café": 12.90}

carrinho:dict = {"maçã": 3, "pão": 2, "leite": 1, "café": 2}

preco_total:int = 0

for chave in precos:
    preco_total += precos[chave] * carrinho[chave]

    print(f'o chave total do produto {chave} é {precos[chave] * carrinho[chave]} ')
    print(f'o preco total é {preco_total}')
    







