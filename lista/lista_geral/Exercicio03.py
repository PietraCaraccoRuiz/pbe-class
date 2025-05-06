dado = 10
avanca = 0
recua = 0

for i in range(dado+1):
    if i  == 4 or i == 7 or i == 10:
        print("\ndado: ", i)
        if i % 2 == 0:
            print("Jogador avança!")
            avanca += 1
        else:
            print("Jogador recua!")
            recua += 1