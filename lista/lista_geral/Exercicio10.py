palavras = ["Ana Ana", "1DSTB-SENAI", "Subi no Onibus"]

for palavra in palavras:

    palavra_limpa = palavra.replace(" ", "").lower()
    quant = len(palavra_limpa)
    normal= []
    invertida = []

    i = 0
    for i in range(quant):
        print(i)
        normal += palavra_limpa[i]
        print(normal)

    j = quant - 1
    for i in range(quant):
        print(j)
        invertida += palavra_limpa[j]
        print(invertida)
        j -= 1

    if normal == invertida:
        print("É palíndromo")
    else:
        print("NÃO é palíndromo")
