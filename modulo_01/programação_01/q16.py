qnt_cigarros_dia = int(input("Qual a quantidade de cigarros vocÊ fuma durante o dia: "))
qnt_anos = int(input("Há quantos anos você fuma: "))
minutos_cigarros = 10
qnt_dias_ano = 365
min_dia = 60 * 24
total_cigarros = qnt_cigarros_dia * qnt_anos * qnt_dias_ano
total_minutos = total_cigarros * minutos_cigarros
dias_perdidos = total_minutos / min_dia
print(f"Se uma pessoa fumar {qnt_cigarros_dia} cigarros por dia durante {qnt_anos} anos, essa pessoa perdeu {dias_perdidos} dias.")