# Fatorial

num = int(input("Digite um número: "))
fat = num

if num >= 0:
    while num != 1:
        print(f"{fat} x {num - 1} = {fat}")
        fat = fat * (num -1)
        num -= 1
else:
    print("Numero negativo! Digite um número positivo.")