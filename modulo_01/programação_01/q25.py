seg1 = float(input("Informe o primerio segmento de reta: "))
seg2 = float(input("Informe o segundo segmento de reta: "))
seg3 = float(input("Informe o terceiro segmento de reta: "))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print("Os segmentos inseridos podem formar um triângulo")
else:
    print("Os segmentos inseridos não podem formar um triângulo")