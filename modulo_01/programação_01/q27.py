nt1 = float(input("Digite a primeria nota: "))
nt2 = float(input("Digite a segunda nota: "))
media = (nt1 + nt2) / 2
if media <= 4.9:
    print("Reprovado")
elif media >= 5.0 and media <= 6.9:
    print("Recuperação")
else:
    print("Aprovado")