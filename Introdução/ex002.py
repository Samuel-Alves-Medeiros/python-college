"""
distância, valor do combustível, quantos litros foram gastos? Valor total gasto, autonomia do veículo.
"""
distancia:float = float(input('Qual foi a distância percorrida? em km?'))
valor_combustivel:float = float(input('Qal o valor/Litro do combustível?'))
litros_gastos:float = float(input('Quantos litros foram gastos na viagem?'))

valor_total_gasto:float = valor_combustivel*litros_gastos
autonomia_do_veiculo:float = distancia/litros_gastos

print(f'o valor total gasto em combustível foi de R${valor_total_gasto}. E a autonomia do veículo é de {autonomia_do_veiculo}Km/litro ')

"""
+
-
*
/
// --> divisão inteira
% --> resto da divisão
** --> potência
"""

"""
==
!=
>
<
>=
<=
Toda expresssão com operadores relacionais retorna um valor booleano
"""