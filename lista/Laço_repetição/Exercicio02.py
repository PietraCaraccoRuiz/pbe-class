# Calcular Soma

numero = int(input("Digite um número: "))
i = 1
soma = 0

if numero > 0:
    while i <= numero:
        print(f"{soma} + {i} =", end=" ")
        soma = soma + i
        print(soma)
        i +=1

    print("A soma é: ", soma)