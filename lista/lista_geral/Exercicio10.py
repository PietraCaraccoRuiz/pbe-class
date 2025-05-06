from operator import invert

palavras = ["Ana Ana", "1DSTB-SENAI", "Subi no Onibus"]

for palavra in palavras:
    quant = len(palavra)
    normal= []
    invertida = []
    for i in range(quant):
        palavra[i]