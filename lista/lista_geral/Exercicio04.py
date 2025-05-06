numeros = [2, 3, 4]

for numero in numeros:
    print("\nTabuada do", numero)
    for i in range (11):
        res = numero * i
        print(f"{numero} x {i} = {res}")