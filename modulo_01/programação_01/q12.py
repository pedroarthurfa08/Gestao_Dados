valor_produto = float(input("Digite o valor do produto: "))
valor_desconto = valor_produto * 0.05
valor_promocao = valor_produto - valor_desconto
print(f"O valor de R${valor_desconto} com o desconto de 5% é igual a R${valor_promocao}")