from operator import invert

palavras = ["Ana Ana", "1DSTB-SENAI", "Subi no Onibus"]

for palavra in palavras:
    quant = len(palavra)
    normal= []
    invertida = []

    i = 0
    for i in range(quant):
        print(i)
        normal += palavra[i]
        print(normal)

    j = quant - 1
    for i in range(quant):
        print(j)
        invertida += palavra[j]
        print(invertida)
        j -= 1

    if normal == invertida:
        print("É palíndromo")
    else:
        print("NÃO é palíndromo")
