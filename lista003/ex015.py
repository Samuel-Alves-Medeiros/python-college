entradas:dict = {"ABC1234": 8, "XYZ9876": 10, "QWE4567": 13, "JKL8899": 9}
hora_atual:int = 15



for k,v in entradas.items():
    print(f'O veículo de código {k} está estacionado há {hora_atual - v} horas')