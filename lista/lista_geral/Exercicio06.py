produtos = [50, 120, 200]

for produto in produtos:
    desconto = produto - (produto * 0.1)
    print(f"Produto {produtos.index(produto)+1} com desconto: R${desconto:.2f}")