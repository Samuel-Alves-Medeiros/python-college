quantidade_pessoa:int = int(input('quantas pessoas moram na sua casa contando com você? '))
renda_total:float = float(input('qual e a renda total da sua família? '))
media_escolar:float = float(input('Qual é a sua média escolar? '))
aulas_total:int = int(input('quantas aulas você teve esse ano?'))
aulas_fraquentadas:int = int(input('Quantas aulas você frenquentou esse ano?'))

renda_percapta:float = renda_total/quantidade_pessoa
frequencia_escolar:int = aulas_fraquentadas * 100 /aulas_total
salario_necessario:float =1621*1.5

print('Você é elegivel para a bolsa' if renda_percapta <=salario_necessario and media_escolar>=7 and
       frequencia_escolar >=75 else 'Você não se aplica para essa bolsa')