status_pedido:list[str] = ["entregue", "pendente","cancelado", "entregue", "pendente", "entregue", "pendente", "cancelado", "entregue", "pendente"]
contador:int = 0

for pedido in status_pedido:
    if pedido == 'pendente':
        contador+=1

print(f'Existem {contador} pedidos pendentes')