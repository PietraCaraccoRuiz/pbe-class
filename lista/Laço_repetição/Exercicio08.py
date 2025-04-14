# Calcule a soma da série harmônica até `N` termos:
# `S = 1 + 1/2 + 1/3 + ... + 1/N.`
# Arredonde o resultado para 2 casas decimais.

numero = int(input("Digite um número: "))
i = 1
s = 1

for i in range(1, numero):
    print(s)
    s = s + (1 / (i + 1))