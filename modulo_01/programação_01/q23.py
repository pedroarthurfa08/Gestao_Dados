nome = input("Informe seu nome: ")
sexo = int(input("Digite '1' para masculino e '2' para feminino."))
valor_compras = float(input("Qual o valor das compras: "))

if sexo == 1:
    valor_desconto_1 = valor_compras * 0.05
    valor_total_1 = valor_compras - valor_desconto_1
    print(f"Senhor {nome} suas compras de R$ {valor_compras} tiveram um desconto no valor R${valor_desconto_1}, deste modo sairam no valor de {valor_total_1}")
elif sexo == 2:
    valor_desconto_2 = valor_compras * 0.05
    valor_total_2 = valor_compras - valor_desconto_2
    print(f"Senhor {nome} suas compras de R$ {valor_compras} tiveram um desconto no valor R${valor_desconto_2}, deste modo sairam no valor de {valor_total_2}")
else:
    print("Sexo Inválido.")