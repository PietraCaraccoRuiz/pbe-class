for i in range(1,13):
    if i == 3 or i == 9 or i == 12:
        print(f"\nNumero {i}: ")
        if i <= 3:
            print("Pequeno")
        elif i <= 9:
            print("Médio")
        else:
            print("Grande")