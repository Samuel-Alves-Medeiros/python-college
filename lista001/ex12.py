preco_produto:float = int(input('Digite o preço do produto e veja seu desconto'))
desconto5:float = preco_produto * 5/100
desconto10:float = preco_produto * 10/100

if preco_produto < 100:
    print('Os descontos só para compras acima de R$100')
elif preco_produto >=100 and preco_produto <500:
    print(f'O preço original é de R${preco_produto}, seu desconto é de R${desconto5} e o preço com desconto é de R${preco_produto - desconto5}')
else:
    print(f'O preço original é de R${preco_produto}, seu desconto é de R${desconto10} e o preço com desconto é de R${preco_produto - desconto10}')