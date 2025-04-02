import math

opcao = int(input("Digite o exercicio: "))

while opcao != 0:
            if opcao == 1:
              # exercicio 1
              nome = "João"
              print(nome)

            elif opcao == 2:
              # exercicio 2
              a = 5
              b = 10
              print(f"\nsoma: {a+b}\nsubtração: {a-b}\nmultiplicação: {a*b}\ndivisão: {a/b}")

            elif opcao == 3:
              # exercicio 3
              preco = 50
              desconto = 10
              print("\nPreço com desconto: ", preco - (preco*(10/100)))

            elif opcao == 4:
              # exercicio 4
              resultado = 10 +  5 * 2
              print(resultado)

            elif opcao == 5:
              #exercicio 5
              texto = "150"
              texto = int(texto)

              print("\n", texto *2)

            elif opcao == 6:
              # exercio 6

              num = [1,2,3,4,5]

              print("\nLista")
              for elemento in num :
                  print(elemento)
              num[2] = 6
              print(num)

            elif opcao == 7:
              # exercicio 7
              valor1 = int(input("Digite o primeiro valor: "))
              valor2 = int(input("Digite o segundo valor: "))
              print("Soma: ", valor1 + valor2)
              
            elif opcao == 8:
              # exercicio 8

              x = int(input("Digite numero: "))
              y = int(input("Digite numero: "))

              print("Divisão: ", x // y)
            elif opcao == 9:
              #exercicio 9

              num1 = int(input("Digite numero: "))
              num2 = int(input("Digite numero: "))

              print(num1 > num2)

            elif opcao == 10:
              # exercicio 10

              idade = int(input("Digite sua idade: "))

              print("Voce viveu aproximadamente ",idade*365, " dias")
            elif opcao == 11:
              #exercicio 11

              base = float(input("Digite a base: "))
              expoente = float(input("Digite o expoente: "))

              print("A area do triangulo é: ", base**expoente)
            elif opcao == 12:
              # exercicio 12

              preco = float(input("Digite o preço: "))
              print("O preço é R$", str(preco))
            elif opcao == 13:
              #exercicio 13

              raio = float(input("Digite o raio: "))

              print("A área do circulo é: ", 3.14*(raio**2))
            elif opcao == 14:
              # exercicio 14

              a = int(input("Digite o primeiro numero: "))
              b = int(input("Digite o segundo numero: "))

              a, b == b, a

              print("\n a: ", a, "\n b: ", b)
            elif opcao == 15:
              # exercicio 15

              nota1 = float(input("Digite a primeira nota: "))
              nota2 = float(input("Digite a segunda nota: "))
              nota3 = float(input("Digite a terceira nota: "))

              media = (3*nota1 + 2*nota2 + 5*nota3) / (3 + 2 + 5)

              print("Media: {:.2f}".format(media))
            elif opcao == 16:
              # exercicio 16

              x1 = int(input("Digite a coordenada x1: "))
              y1 = int(input("Digite a coordenada y1: "))
              x2 = int(input("Digite a coordenada x2: "))
              y2 = int(input("Digite a coordenada y2: "))

              x = (x2 - x1)**2
              y = (y2 - y1)**2
              raiz = math.sqrt(x + y)
              raiz1 = (x + y)**0.5

              print(f"A distancia entre dois esses dois pontos é: {raiz:.2f}")
              print(f"A distancia entre dois esses dois pontos é: {raiz1:.2f}")
            else:
              print("\nOpção invalida")
            opcao = int(input("\nDigite o exercicio: \nPara sair digite 0"))
            