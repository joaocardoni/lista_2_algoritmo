# Uma professora precisa registrar a presença dos alunos durante a semana.
# • Cada dia da semana terá uma lista com os nomes dos presentes.
# • No final, ela precisa:
# 1. Saber quais alunos estiveram presentes todos os dias.
# 2. Saber quais alunos faltaram em pelo menos um dia.
# 3. Saber o número total de presenças por aluno.

def lista_dia(quant):
    lista_d=[]
    for a in range (quant):
        add_aluno = input("Diga o nome do aluno que veio:")
        lista_d.append(add_aluno)
    return lista_d


quant_d1=int(input("Diga quantos alunos estiveram presentes no 1° dia"))
lista_d1=lista_dia(quant_d1)

quant_d2=int(input("Diga quantos alunos estiveram presentes no 2° dia"))
lista_d2=lista_dia(quant_d2)

quant_d3=int(input("Diga quantos alunos estiveram presentes no 3° dia"))
lista_d3=lista_dia(quant_d3)

quant_d4=int(input("Diga quantos alunos estiveram presentes no 4° dia"))
lista_d4=lista_dia(quant_d4)

quant_d5=int(input("Diga quantos alunos estiveram presentes no 5° dia"))
lista_d5=lista_dia(quant_d5)



lista_contagem=[]

for i in lista_d1:
    lista_contagem.append(i)
for i in lista_d2:
    lista_contagem.append(i)
for i in lista_d3:
    lista_contagem.append(i)
for i in lista_d4:
    lista_contagem.append(i)
for i in lista_d5:
    lista_contagem.append(i)
lista_total=[]
for i in lista_d1:
    cont=lista_total.count(i)
    if cont == 0:
        lista_total.append(i)
for i in lista_d2:
    cont=lista_total.count(i)
    if cont == 0:
        lista_total.append(i)
for i in lista_d3:
    cont=lista_total.count(i)
    if cont == 0:
        lista_total.append(i)
for i in lista_d4:
    cont=lista_total.count(i)
    if cont == 0:
        lista_total.append(i)
for i in lista_d5:
    cont=lista_total.count(i)
    if cont == 0:
        lista_total.append(i)


lista_falta=[]
lista_presenca_total=[]
for i in lista_contagem:
    a=lista_contagem.count(i)
    if a == 5:
        b=lista_presenca_total.count(i)
        if b ==0:
            lista_presenca_total.append(i)
    else:
        c = lista_falta.count(i)
        if c == 0:
            lista_falta.append(i)
    
aluno_procurado = input("Digite o nome do aluno que gostaria de saber a quantidade de presença:")
presenca_aluno_procurado = lista_contagem.count(aluno_procurado)



print(f'A lista total será {lista_total}\n Os alunos que não faltaram são {lista_presenca_total}\n Os alunos que faltaram ao menos um dia são {lista_falta}\n O(A) {aluno_procurado} esteve presente em {presenca_aluno_procurado} dias')
#indice=lista.count('arroz')
#print (indice)