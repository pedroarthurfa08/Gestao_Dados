def limpar_tela():
    import os,sys
    # Verifica o sistema operacional
    if sys.platform.startswith('win'):  # Se for Windows
        os.system('cls')
    else:  # Para Linux e macOS
        os.system('clear')

titulo=\
'''---------------------------------------------------------
CURSO SUPERIOR DE TECNOLOGIA EM GESTÃO DE DADOS/UFPI/CEAD
DISCIPLINA: PROGRAMAÇÃO I
DISCENTE: PEDRO ARTHUR FONTENELE ALVES
MATRÍCULA: 20259076981
---------------------------------------------------------'''

def questao1():
    print('\n','Questão 1.'.center(40,'-'))
    print('Olá Mundo!')

def questao2():
    print('\n','Questão 2.'.center(40,'-'))
    nome=input('Qual o seu nome?')
    print(f'Olá {nome}, é um prazer te conhecer!')

def questao3():
    nome = input("Nome do Funcionário: ")
    salario = float(input("Salário: "))
    print(f"O funcionário(a) {nome} tem um salário de {salario} em setembro.")

def questao4():
    print('\n','Questão 4.'.center(40,'-'))
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))
    x = n1 + n2
    print(f'A soma entre {n1} e {n2} é igual a {x}')

def questao5():
    nt1 = float(input("Digite a primeria nota: "))
    nt2 = float(input("Digite a segunda nota: "))
    x = (nt1 + nt2) / 2
    print(f"A média da nota 1: {nt1} e da nota 2: {nt2} é igual a {x}")

def questao6():
    print('\n','Questão 6.'.center(40,'-'))
    n = int(input("Digite um número: "))
    antecessor = n - 1
    sucessor = n + 1
    print(f"O antecessor de {n} é {antecessor}.")
    print(f"O sucessor de {n} é {sucessor}.")

def questao7():
    print('\n','Questão 7.'.center(40,'-'))
    n = float(input("Digite um número: "))
    dobro = n * 2
    terca_parte = n / 3
    print(f"O dobro de {n} é {dobro}.")
    print(f"A terça parte de {n} é {terca_parte}.")

def questao8():
    print('\n','Questão 8.'.center(40,'-'))
    metros = float(input("Digite a diatâcia em metros: "))
    km = metros / 1000
    hm = metros / 100
    dam = metros / 10
    dm = metros * 10
    cm = metros * 100
    mm = metros * 1000
    print(f"A ditância de {metros}m corresposnde a:")
    print(f"{km} Km")
    print(f"{hm} Hm")
    print(f"{dam} Dam")
    print(f"{dm} dm")
    print(f"{cm} cm")
    print(f"{mm} mm")

def questao9():
    print('\n','Questão 9.'.center(40,'-'))
    reais = float(input("Dinheiro total na carteira em reais:"))
    dolares = reais / 3.45
    print(f"Pode comprar {dolares} dólares com {reais} reaias.")

def questao10():
    print('\n', 'Questão 10.'.center(40,'-'))
    largura = float(input("Digite a largura da parede: "))
    altura = float(input("Digite a altura da parede: "))
    area = largura * altura
    litro = area / 2 
    print(f"Para pintar a parede de {area} metros é necessário {litro} litros.")

def questao11():
    print('\n', 'Questão 11.'.center(40,'-'))
    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))
    delta = b ** 2 - 4 * a * c
    print(f"O valor de delta é {delta}")

def questao12():
    print('\n', 'Questão 12.'.center(40,'-'))
    valor_produto = float(input("Digite o valor do produto: "))
    valor_desconto = valor_produto * 0.05
    valor_promocao = valor_produto - valor_desconto
    print(f"O valor de R${valor_desconto} com o desconto de 5% é igual a R${valor_promocao}")

def questao13():
    print('\n', 'Questão 13.'.center(40,'-'))
    salario_atual = float(input("Qual o valor do salário: "))
    valor_aumento = salario_atual * 0.15
    valor_total = salario_atual + valor_aumento
    print(f" O salário antigo de R${salario_atual} com a promoção de 15% fica no valo de R${valor_total}")

def questao14():
    print('\n', 'Questão 14.'.center(40,'-'))
    km_percorridos = float(input("Qual a quantidade e kms percorridos: "))
    dias_rodados = int(input("Qual a quantidade de dias rodados: "))
    valor_km = km_percorridos * 0.20
    valor_dia = dias_rodados * 90
    valor_total = valor_km + valor_dia
    print(f"O valor total a ser pago andando {km_percorridos}kms durante {dias_rodados} dias, é de R$ {valor_total}")

def questao15():
    print('\n', 'Questão 15.'.center(40,'-'))
    dias_trabalhados = int(input("Qual a quantidade de dias trabalhados: "))
    qnt_horas_mes = dias_trabalhados * 8
    salario_mes = qnt_horas_mes * 25
    print(f"Se o funcionário trabalhou durante {dias_trabalhados} dias, ele receberá R${salario_mes}.")

def questao16():
    print('\n', 'Questão 16.'.center(40,'-'))
    qnt_cigarros_dia = int(input("Qual a quantidade de cigarros vocÊ fuma durante o dia: "))
    qnt_anos = int(input("Há quantos anos você fuma: "))
    minutos_cigarros = 10
    qnt_dias_ano = 365
    min_dia = 60 * 24
    total_cigarros = qnt_cigarros_dia * qnt_anos * qnt_dias_ano
    total_minutos = total_cigarros * minutos_cigarros
    dias_perdidos = total_minutos / min_dia
    print(f"Se uma pessoa fumar {qnt_cigarros_dia} cigarros por dia durante {qnt_anos} anos, essa pessoa perdeu {dias_perdidos} dias.")
def questao17():
    print('\n', 'Questão 17.'.center(40,'-'))
    vel_carro = float(input("Digite e velocidade do carro em km/h: "))
    vel_max = 80
    valor_multa_km = 5
    if vel_carro > vel_max:
        ultrapassa_vel = vel_carro - vel_max
        multa = ultrapassa_vel * valor_multa_km
        print(f"Velocidade de {ultrapassa_vel} km/h, portanto receberá multa no valor de R${multa} ")
    else:
        print(f"Velocidade dentro do limete da via, portanto sem multas.")

def questao18():
    print('\n', 'Questão 18.'.center(40,'-'))
    ano = int(input("Digite o ano do seu nascimento: "))
    idade = 2025 - ano
    if idade > 16:
        print("Você está apto a votar.")
    else:
        print("Você não está apto a votar.")

def questao19():
    print('\n', 'Questão 19.'.center(40,'-'))
    nt1 = float(input("Digite a primeria nota: "))
    nt2 = float(input("Digite a segunda nota: "))
    media = (nt1 + nt2) / 2
    print(f"Média igual a {media}")
    if media > 7 :
        print("Aluno teve um bom aproveitamento.")
    else:
        print("Aluno não teve um bom aproveitamento.")

def questao20():
    print('\n', 'Questão 20.'.center(40,'-'))
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        print("Este número é PAR.")
    else:
        print("Este número é IMPAR.")

def questao21():
    print('\n', 'Questão 21.'.center(40,'-'))
    ano = int(input("Digite um ano: "))
    if (ano % 4 == 0 and ano % 100 != 0 ) or (ano % 400 == 0):
        print(f"O ano {ano} é BISSEXTO")
    else:
        print(f"O ano {ano} não é BISSEXTO")

def questao22():
    print('\n', 'Questão 22.'.center(40,'-'))
    ano_atual = int(input("Informe o ano atual: "))
    ano_nascimento = int(input("Informe o seu ano de nascimento: "))
    idade = ano_atual - ano_nascimento
    if idade < 18:
        falta = 18 - idade
        print(f"Falta {falta} para o seu alistamento.")
    elif idade > 18:
        passou = idade - 18
        print(f"Passou {passou} do o seu alistamento.")
    else:
        print("Você deve se alistar esse ano")

def questao23():
    print('\n', 'Questão 23.'.center(40,'-'))
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

def questao24():
    print('\n', 'Questão 24.'.center(40,'-'))
    distancia = float(input("Qual será a distância que você deseja percorrer em km? "))
    if distancia <= 200:
        passagem = distancia * 0.50
    else:
        passagem = distancia * 0.40
    print(f"O preço da passagem para {distancia:.1f} km é R$ {passagem:.2f}") 

def questao25():
    print('\n', 'Questão 25.'.center(40,'-'))
    seg1 = float(input("Informe o primerio segmento de reta: "))
    seg2 = float(input("Informe o segundo segmento de reta: "))
    seg3 = float(input("Informe o terceiro segmento de reta: "))
    if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
        print("Os segmentos inseridos podem formar um triângulo")
    else:
        print("Os segmentos inseridos não podem formar um triângulo")

def questao26():
    print('\n', 'Questão 26.'.center(40,'-'))
    n1 = int(input("Informe o primeiro número: "))
    n2 = int(input("Informe o segundo número: "))
    if n1 > n2:
        print("O primeiro valor é o maior.")
    elif n2 > n1:
        print("O segundo valor é o maior.")
    else: 
        print("Não existe valor maior, os dois são iguais.")

def questao27():
    print('\n', 'Questão 27.'.center(40,'-'))
    nt1 = float(input("Digite a primeria nota: "))
    nt2 = float(input("Digite a segunda nota: "))
    media = (nt1 + nt2) / 2
    if media <= 4.9:
        print("Reprovado")
    elif media >= 5.0 and media <= 6.9:
        print("Recuperação")
    else:
        print("Aprovado")

def questao28():
    print('\n', 'Questão 28.'.center(40,'-'))
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

def questao29():
    print('\n', 'Questão 29.'.center(40,'-'))
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

def questao30():
    print('\n', 'Questão 30.'.center(40,'-'))
    seg1 = float(input("Informe o primerio segmento de reta: "))
    seg2 = float(input("Informe o segundo segmento de reta: "))
    seg3 = float(input("Informe o terceiro segmento de reta: "))
    if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
        print("Os segmentos inseridos podem formar um triângulo")
        if seg1 == seg2 == seg3:
            print("EQUILÁTERO: todos os lados iguais")
        elif seg1 == seg2 or seg2 == seg1 or seg2 == seg3:
            print("ISÓSCELES: dois lados iguais")
        else: 
            print("ESCALENO: todos os lados diferentes ")

            print("Os segmentos inseridos podem formar um triângulo")
    else:
        print("Os segmentos inseridos não podem formar um triângulo")

def questao31():
    print('\n', 'Questão 31.'.center(40,'-'))
    import random
    def escolha_usuario():
        escolha = input("Escolha Pedra, Papel ou Tesoura (ou 'sair' para encerrar): ").strip().lower()
        if escolha in ("pedra", "papel", "tesoura"):
            return escolha
        elif escolha == "sair":
            return None
        else:
            print("Escolha inválida, tente novamnete.")
            return escolha_usuario()
    def escolha_computador():
        return random.choice(["pedra", "papel", "tesoura"])
    def vencedor(usuario, computador):
        if usuario == computador:
            return "Empate!"
        elif (usuario == "pedra" and computador == "tesoura") or \
            (usuario == "tesoura" and computador == "papel") or \
            (usuario == "papel" and computador == "pedra"):
            return "Você venceu!"
        else:
            return "Você perdeu e o pc ganhou!"  
    def main():
        print("Bem-vindo ao jogo Pedra, Papel e Tesoura!")
        while True:
            usuario = escolha_usuario()
            if usuario is None:
                print("Encerrando o jogo...")
                break
            computador = escolha_computador()
            print(f"Computador escolheu: {computador}")
            resultado = vencedor(usuario, computador)
            print(resultado)
    main()

def questao32():
    print('\n', 'Questão 32.'.center(40,'-'))

def questao33():
    print('\n', 'Questão 33.'.center(40,'-'))

def executa(opcao):
    acoes={
        '1':questao1,
        '2':questao2,
        '3':questao3,
        '4':questao4,
        '5':questao5,
        '6':questao6,
        '7':questao7,
        '8':questao8,
        '9':questao9,
        '10': questao10,
        '11': questao11,
        '12': questao12,
        '13': questao13,
        '14': questao14,
        '15': questao15,
        '16': questao16,
        '17': questao17,
        '18': questao18,
        '19': questao19,
        '20': questao20,
        '21': questao21,
        '22': questao22,
        '23': questao23,
        '24': questao24,
        '25': questao25,
        '26': questao26,
        '27': questao27,
        '28': questao28,
        '29': questao29,
        '30': questao30,
        '31': questao31,
        '32': questao32,
        '33': questao33,
        #fazer até última questão
    }
    if opcao in acoes:#executa se a opcao foi cadastrada
        acoes[opcao]()
    else:
        print(f"\nOpção {op} não cadastrada")
    tempo=input("\nPressione Enter para continuar...")

if __name__=='__main__':
    while True:
        limpar_tela()
        print(titulo)
        print('\t Escolha uma questão [1-33]')
        print('\t Digite 0 (zero) para sair.')
        op=input("\t Escolha: ")
        if op=='0': 
            print('\nFinalizando o programa.\n')
            break
        executa(op)