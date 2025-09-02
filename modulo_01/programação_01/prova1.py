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
DISCENTE: PEDRO ARTHUR FONTENELE
MATRÍCULA: XXXXXXXXXXX
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

def questao18():
    print('\n', 'Questão 18.'.center(40,'-'))

def questao19():
    print('\n', 'Questão 19.'.center(40,'-'))

def questao20():
    print('\n', 'Questão 20.'.center(40,'-'))

def questao21():
    print('\n', 'Questão 21.'.center(40,'-'))

def questao22():
    print('\n', 'Questão 22.'.center(40,'-'))

def questao23():
    print('\n', 'Questão 23.'.center(40,'-'))

def questao24():
    print('\n', 'Questão 24.'.center(40,'-'))

def questao25():
    print('\n', 'Questão 25.'.center(40,'-'))

def questao26():
    print('\n', 'Questão 26.'.center(40,'-'))

def questao27():
    print('\n', 'Questão 27.'.center(40,'-'))

def questao28():
    print('\n', 'Questão 28.'.center(40,'-'))

def questao29():
    print('\n', 'Questão 29.'.center(40,'-'))

def questao30():
    print('\n', 'Questão 30.'.center(40,'-'))

def questao31():
    print('\n', 'Questão 31.'.center(40,'-'))

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