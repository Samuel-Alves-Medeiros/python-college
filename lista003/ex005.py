funcionario:dict = {"nome": "Marcos", "cargo": "Analista", "salario": 3200.00}

reajuste:float = funcionario['salario'] + funcionario["salario"] * (8/100)

funcionario["salario"] = reajuste

print(f'Seu novo salário é {funcionario["salario"]}')