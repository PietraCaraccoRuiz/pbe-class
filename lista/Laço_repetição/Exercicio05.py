# Peça ao usuário um número e verifique se ele é primo usando um laço.
# Um número primo é divisível apenas por 1 e por ele mesmo.
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29

numero = int(input("Digite um numero: "))
primos = []

for j in range(1, numero + 1):
    cont = 0
    for i in range(1, numero + 1):
        if j % i == 0:
            cont += 1

    if cont == 2:
        primos.append(j)

print("Números primos: ", primos)