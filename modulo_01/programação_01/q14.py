km_percorridos = float(input("Qual a quantidade e kms percorridos: "))
dias_rodados = int(input("Qual a quantidade de dias rodados: "))
valor_km = km_percorridos * 0.20
valor_dia = dias_rodados * 90
valor_total = valor_km + valor_dia
print(f"O valor total a ser pago andando {km_percorridos}kms durante {dias_rodados} dias, é de R$ {valor_total}")