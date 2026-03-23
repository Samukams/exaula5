salario = 1200
c1 = 200
c2 = 120

multa1 = c1 * 0.02
multa2 = c2 * 0.02

total_c1 = c1 + multa1
total_c2 = c2 + multa2

restante = salario - (total_c1 + total_c2)


print(f"Sobrará na conta de João {restante} reais")