carrinho:list[float] = [49.90, 120.00, 15.50, 8.99,32.00, 75.00, 19.99, 5.50, 60.00, 22.30]
soma:float = 0 
desconto:float = 0

for produto in carrinho:
    soma+= produto

if soma >300:
    desconto = soma*10/100

print(f'O valor total do seu carrinho é de R${soma-desconto:.2f} ')