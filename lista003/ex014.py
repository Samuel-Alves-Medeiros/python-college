paciente:dict = {"nome": "Carlos", "idade": 40, "alergias": ["dipirona", "poeira", "amendoim"]}

nome:str = paciente["nome"]
alergias:list[str] = paciente["alergias"]

print(f'O paciente {nome} te alergia a:')
for alergia in alergias:
    print(alergia)