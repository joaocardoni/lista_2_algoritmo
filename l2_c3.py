# Um supermercado mantém uma lista de produtos e seus preços.
# • Cada item será representado como [nome, quantidade, preco_unitario].
# • O sistema deve:
# 1. Calcular o valor total em estoque.
# 2. Encontrar o produto de maior valor total (quantidade × preço).
# 3. Gerar uma lista apenas com os nomes dos produtos com estoque abaixo de 5
# unidades.
# 4. Permitir buscar um produto pelo nome e retornar seus dados.

estoque =[['arroz', 5, 9],['feijao', 3, 2],['batata', 5, 30],['carne', 7, 4]]




tam_estoque = len(estoque)
valor_em_estoque = 0
valor_total = 0
produto_valor_total = ''
lista_prod_abaixo =[]
for i in estoque:
    valor_especifico_estoque = i[1]*i[2]
    valor_em_estoque = valor_em_estoque + valor_especifico_estoque
    produto = i[1]*i[2]
    if produto > valor_total:
        produto_valor_total = i[0]
    if i[2] < 5:
        lista_prod_abaixo.append(i[0])     

procura = input("Diga qual produto gostaria de procurar:")

resultado = None
for i in estoque:
    if i[0] == procura:
        resultado = i


print(f" O valor em estoque é {valor_em_estoque}, o produto de maior valor é {produto_valor_total}, a lista de produtos com estoque abaixo de 5 é {lista_prod_abaixo}, e o resultado de sua pesquisa é {resultado}")
    


