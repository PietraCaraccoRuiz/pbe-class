# Peça ao o usuário um numero `N`. E o utilize laços aninhados para imprimir o seguinte padrão :
# `N = 5`
# ```
# *
# **
# ***
# ****
# *****
# ```

numero = int(input("Digite um número: "))

ponto = ""

for i in range(numero):
    ponto += "*"
    print(ponto)