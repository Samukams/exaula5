m1 = int(input("Quantidade de moedas de 1 centavo: "))
m5 = int(input("Quantidade de moedas de 5 centavos: "))
m10 = int(input("Quantidade de moedas de 10 centavos: "))
m25 = int(input("Quantidade de moedas de 25 centavos: "))
m50 = int(input("Quantidade de moedas de 50 centavos: "))
m1real = int(input("Quantidade de moedas de 1 real: "))

v1 = m1 * 0.01
v5 = m5 * 0.05
v10 = m10 * 0.10
v25 = m25 * 0.25
v50 = m50 * 0.50
v1real = m1real * 1

valorTotal = v1 + v5 + v10 + v25 + v50 +v1real

print(f"Total economizado é: {valorTotal}")