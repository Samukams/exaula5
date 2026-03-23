anoN = int(input("Informe o seu ano de nascimento: "))
anoAtual = int(input("Informe o ano atual:"))

a = anoAtual - anoN
b = anoAtual * 12
c = a * 365
d = a * 52

print(f"Você tem {a} anos de idade\nVocê tem {b} meses de idade\nVocê tem {c} dias de idade\nVocê tem {d} semanas de idade")