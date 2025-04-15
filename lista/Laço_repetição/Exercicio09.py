# Implemente um algoritmo que encontre e imprima todos os números de Kaprekar em um intervalo definido pelo usuário (ex: 1 a 10000).
# Onde você irá solicitar os 2 numeros do intervalo

perfeitos = []

for i in range(1,1001):
    soma = 0
    for j in range(1,1001):
        if i == j:
            break

        if i % j == 0:
            soma = soma + j
    if soma == i:
        perfeitos.append(i)

print("Números Perfeitos: ", perfeitos)