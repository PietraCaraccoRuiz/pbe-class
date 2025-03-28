import re

opcao = 20

while opcao != 0:

    opcao = int(input("Digite o exercicio: "))

    if opcao == 1:
        numero =int(input("Digite um número: "))
        if numero % 2 == 0:
            print("Par")
        else:
            print("Impar")
    elif opcao == 2:
        numero = int(input("Digite um número: "))
        if numero > 10:
            print("Número maior que 10")
        else:
            print("Numero menor que 10")
    elif opcao == 3:
        idade = int(input("Digite sua idade: "))
        if idade < 18:
            print("Menor de idade")
        else:
            print("Maior de idade")
    elif opcao == 4:
        idade = int(input("Digite sua idade: "))
        if (16 <= idade < 18) or idade > 70:
            print("Voto opcional")
        elif idade >= 18:
            print("Voto obrigatório")
        elif idade < 16:
            print("nao voto")
    elif opcao == 5:
        numero= int(input("Digite um número: "))
        if numero > 0:
            print("Número positivo")
        elif numero < 0:
            print("Número negativo")
        else:
            print("Núemro 0")
    elif opcao == 6:
        nota = float(input("Digite a nota: "))
        if 0 <= nota <= 10:
            if 9 <= nota:
                print("nota A")
            elif 7 <= nota:
                print("nota B")
            elif  5 <= nota:
                print("nota C")
            elif 3 <= nota:
                print("nota D")
            elif nota <= 2:
                print("nota E")
        else:
            print("Opcao invalida! Digite um número de 1 a 10: ")
    elif opcao == 7:
        idade = int(input("Digite sua idade: "))
        if idade <= 12 or idade > 60:
            print("Desconto!")
        else:
            print("Sem desconto!")
    elif opcao == 8:
        lado1 = float(input("Digite um lado: "))
        lado2 = float(input("Digite um lado: "))
        lado3 = float(input("Digite um lado: "))
        lado4 = float(input("Digite um lado: "))

        if lado1 == lado2 == lado3 == lado4:
            print("É quadrado")
        elif (lado1 == lado2 or lado3 == lado4) or (lado1 == lado3 or lado2 == lado4) or (
                lado2 == lado3 or lado1 == lado4):
            print("Retangulo")
        else:
            print("Nehnum dos dois")
    elif opcao == 9:
        valor = float(input("Digite o valor total da compra: "))

        if valor < 100:
            desconto = 5 / 100
        elif 100 <= valor <= 500:
            desconto = 10 / 100
        else:
            desconto = 15 / 100

        # Exibe o valor do desconto e o valor final com desconto
        print("\nDesconto:", valor * desconto)
        print("Valor com desconto:", valor - (valor * desconto))

    elif opcao == 10:
        ano = int(input("Digite um ano: "))
        if ano % 4 == 0 or ano % 100 != 0 and ano % 400 == 0:
                print("A ano é bissexto")
        else:
            print("A não é bissexto")

    elif opcao == 11:
        peso = float(input("Qual é o peso(kg): "))
        altura = float(input("Qual é a altura(m): "))
        imc = peso / altura**2
        print(f"Seu IMC é: {imc:.2f}")
        if imc < 18.5:
            print("Baixo peso")
        elif 18.5 < imc < 24.9:
            print("Normal")
        elif 25 < imc < 29.9:
            print("Sobrepeso")
        elif 30 < imc < 34.9:
            print("Obesidade")
        elif 35 < imc < 39.9:
            print("Obesidade Mórbida")
        elif imc > 40:
            print("Obesidade Mórbida")
        else:
            print("Nenhum")

    elif opcao == 12:
        numero1 = int(input("Digite um número"))
        numero2 = int(input("Digite outro número"))
        numero3 = int(input("Digite outro número"))

    elif opcao == 13:
        celsius = float(input("Digite o graus celsius: "))

        if celsius <= 10:
            print("Frio!")
        elif celsius <= 25:
            print("Aconchegante!")
        elif celsius <= 40:
            print("Quente!")
        else:
            print("Muito quente!")
    
    elif opcao == 14:
        data = input("Digite uma data no formato dd/mm/aaaa: ")

        dia, mes, ano = data.split('/')

        data_formatada = f"{ano}/{mes}/{dia}"

        print("Data no formato aaaa/mm/dd:", data_formatada)

    elif opcao == 15:
        senha = input("Digite a senha: ")
        
        if (len(senha) >= 8 and
            re.search(r'[A-Z]', senha) and
            re.search(r'[a-z]', senha) and
            re.search(r'\d', senha) and
            re.search(r'[@#$%&]', senha)):
            print("Senha válida!")
        else:
            print("Senha inválida!")

    elif opcao == 16:
        numero = float(input("Digite um numero: "))

        if numero < 0:
            print("Não é possivel calcular raiz quadrada de um número negativo")
        elif numero > 100:
            print("Número muito grande! reduza para um número menor que 100")
        else:
            raiz_quadrada = numero ** (1/2)
            print(f"Raiz quadrada: {raiz_quadrada:.2f}")
    elif opcao == 17:
        data = input("Digite uma data no formato dd/mm/aaaa: ")

        dia, mes, ano = data.split('/')

        dia = int(dia)
        mes = int(mes)
        ano = int(ano)


        if 1 <= mes < 12:
            if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                if dia <= 31:
                    data_formatada = f"{ano}/{mes:02d}/{dia:02d}"
                else:
                    print("Data inválida!")
            elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
                if dia <= 30:
                    data_formatada = f"{ano}/{mes:02d}/{dia:02d}"
                else:
                    print("Data inválida!")
            elif mes == 2:
                if dia == 28 or dia == 29:
                    data_formatada = f"{ano}/{mes:02d}/{dia:02d}"
                else:
                    print("Data inválida!")
            print("Data no formato aaaa/mm/dd:", data_formatada)
        else:
            print("Mês inválido! Digie um mês de 1 a 12")


    opcao = int(input("Deseja continuar: "))