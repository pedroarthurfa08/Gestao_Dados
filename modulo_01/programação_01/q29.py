nome = input("Digite seu nome: ")
salario = float(input("Informe seu salário: "))
temp_empresa = int(input("Quantos anos de trabalho na empresa: "))
n_salario_1 = (salario * 0.03) + salario
n_salario_2 = (salario * 0.125) + salario
n_salario_3 = (salario * 0.20) + salario

if temp_empresa <= 3:
    print(f"Senhor(a) {nome}, com o ajuste de 3% seu novo salário será de R$ {n_salario_1}.")
elif temp_empresa <= 10:
    print(f"Senhor(a) {nome}, com o ajuste de 12,5% seu novo salário será de R$ {n_salario_2}.")
elif temp_empresa >= 10:
    print(f"Senhor(a) {nome}, com o ajuste de 20% seu novo salário será de R$ {n_salario_3}.")
else:
    print("Informe uma quantidade de anos correta.")