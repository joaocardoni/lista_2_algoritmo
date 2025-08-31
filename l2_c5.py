# Os organizadores de um evento registraram os nomes dos participantes de cada atividade em
# listas separadas.
# • Exemplo:
# o Palestra: ["Ana", "Carlos", "Marina"]
# o Workshop: ["Carlos", "João", "Ana"]
# o Mesa-redonda: ["Marina", "João", "Paula"]
# Eles precisam:
# 1. Saber quem participou de todas as atividades.
# 2. Saber quem participou de apenas uma atividade.
# 3. Gerar uma lista com todos os nomes únicos dos participantes.
# 4. Contar quantos participantes distintos houve no evento.


palestra=[]
workshop =[]
mesa=[]


def participante(palestra, workshop, mesa):

    lista_total=[]


    for i in palestra:
        validacao = i in lista_total
        if validacao == False:
            lista_total.append(i)
        


    for i in workshop:
        validacao = i in lista_total
        if validacao == False:
            lista_total.append(i)


    for i in mesa:
        validacao = i in lista_total
        if validacao == False:
            lista_total.append(i)


    lista_presenca_total=[]

    lista_apenas_um=[]

    for i in palestra:
        if i in workshop:
            if i in mesa:
             lista_presenca_total.append(i)
    for i in palestra:
        if i not in workshop:
            if i not in mesa:
                lista_apenas_um.append(i)
    for i in workshop:
        if i not in palestra:
            if i not in mesa:
                lista_apenas_um.append(i)
    for i in mesa:
        if i not in workshop:
            if i not in palestra:
                lista_apenas_um.append(i)

    contagem = len(lista_total)
    resulta = [lista_total, lista_presenca_total, lista_apenas_um, contagem]
    return resulta

fun=participante(palestra, workshop, mesa)
lista_total = fun[0]
lista_presenca_total = fun[1]
lista_apenas_um=fun[2]
contagem=fun[3]

print(lista_total, lista_presenca_total, lista_apenas_um, contagem)