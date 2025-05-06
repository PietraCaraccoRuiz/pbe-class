palavras = ["casa", "paralelepípedo", "python"]
letras = 0

for palavra in palavras:
    for i in palavra:
            letras += 1
    print(f"A palavra {palavra} tem {letras}")
    letras = 0