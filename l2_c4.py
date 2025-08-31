# Uma loja online registra o número de vendas de cada dia do mês em uma lista.
# • Exemplo: [10, 15, 20, 5, 0, 8, ...]
# O gerente precisa:
# 1. Calcular o total de vendas no mês.
# 2. Descobrir o dia com mais vendas e o dia com menos vendas.
# 3. Calcular a média de vendas por dia.
# 4. Listar os dias que tiveram vendas acima da média.[
    
  



def vendas(lista_vendas):

    total_vendas = 0
    for i in lista_vendas:
        total_vendas = total_vendas + i
    total_dias = len(lista_vendas)
    maior_venda=max(lista_vendas)
    menor_venda=min(lista_vendas)
    dia_maior = lista_vendas.index(maior_venda) +1
    dia_menor = lista_vendas.index(menor_venda) +1


    media = total_vendas/total_dias

    lista_maior_media=[]

    for i in lista_vendas:
        if i > media:
         indice = lista_vendas.index(i) +1
         lista_maior_media.append(indice)
    retorno = [total_vendas, dia_maior, dia_menor, media, lista_maior_media]
    return retorno

def lista_vendas(dias):
   lista_total=[]
   for i in range (dias):
      indice = i+1
      vendas = int(input(f"Diga quantas vendas foram feitas no {indice}° dia"))
      lista_total.append(vendas)
   return lista_total    



dias=int(input("Diga quantos dias foram trabalhados"))
lista_vendas=lista_vendas(dias)

resultado = vendas(lista_vendas)
total = resultado[0]
d_maior = resultado[1]
d_menor = resultado[2]
media = resultado[3]
lista_maiores = resultado[4]


print(f"O total de vendas foi {total} vendas,\n o dia com maior vendas foi o {d_maior}° dia,\n o dia com menor vendas foi o {d_menor}° dia,\n a média de vendas foi {media} vendas e\n os dias acima da média de vendas foram os seguintes dias: {lista_maiores}")

