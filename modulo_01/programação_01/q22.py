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