distancia = float(input("Qual será a distância que você deseja percorrer em km? "))
if distancia <= 200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45
print(f"O preço da passagem para {distancia:.1f} km é R$ {passagem:.2f}") 