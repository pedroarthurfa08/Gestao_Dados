largura = float(input("Informe a largura do terreno: "))
comprimento = float(input("Informe a comprimento do terreno: "))
area = largura * comprimento
print(f"Área do terreno: {area:.2f} m²")
if area < 100:
    print("TERRENO POPULAR")
elif area < 500:
    print("TERRENO MASTER")
else :
    print("TERRENO VIP")