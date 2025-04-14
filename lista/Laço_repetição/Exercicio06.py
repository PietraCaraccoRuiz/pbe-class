# Peça ao usuário um número `N` e gere os primeiros `N` termos da sequência
# de Fibonacci usando um laço.
# Exemplo: `0, 1, 1, 2, 3, 5, 8....`

numero = int(input("Digite um número: "))
soma = 1
a = 1
i = 1
fibonacci = []

fibonacci.append(soma)
while soma < numero:
    fibonacci.append(soma)
    soma = a + i
    a = i
    i = soma

    if soma == 2:
        fibonacci.append(soma)
        soma = a + i
        a = i
        i = soma

print("Sequencia Fibonacci: ", fibonacci)