# número de Kaprekar

K = int(input("Digite um número: "))
kaprekar = False
par = False
impar = False

condicao = K ** 2
print("\nK² = ",condicao)
condicao_string = str(condicao)
length = len(condicao_string)
meio = int(length / 2)
right_side = ""
left_side = ""
comparacao = ""


for i in range(meio):
    print(condicao_string[i])
    left_side += condicao_string[i]

for i in range(meio, length):
    right_side += condicao_string[i]
    comparacao += "0"
if right_side == comparacao:
    kaprekar = False
    print("Lado direito termina com ", comparacao)

if meio <= 0:
    meio = 1
    left_side = "0"
    right_side = condicao

soma = int(right_side) + int(left_side)

if soma == K:
    kaprekar = True

if kaprekar:
    print(f"O número {K} é considerado Kaprekar")
else:
    print(f"O número {K} NÃO é considerado Kaprekar")
