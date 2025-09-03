vel_carro = float(input("Digite e velocidade do carro em km/h: "))
if vel_carro > 80:
    ultrapassar_vel = vel_carro - 80
    multa = ultrapassar_vel * 5
    print(f"Velocidade de {ultrapassar_vel} km/h, portanto receberá multa no valor de R${multa} ")
else:
    print(f"Velocidade dentro do limete da via, portanto, sem multas.")