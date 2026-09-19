horas_do_dia:int = 231 % 24 #// O resto da divisão vai ser a quantidade de horas que sobram.


if horas_do_dia >5 and horas_do_dia<=12:
    print(f'A missão retornou às {horas_do_dia}h no período da manhã')
elif horas_do_dia >12 and horas_do_dia <=18:
    print(f'A missão retornou às {horas_do_dia}h no período da tarde')
else:
    print(f'A missão retornou às {horas_do_dia}h no período da noite')

