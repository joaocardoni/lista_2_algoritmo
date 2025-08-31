# Uma biblioteca mantém uma lista de livros emprestados, onde cada item é representado por
# [titulo, usuario, dias_emprestado].
# Exemplo:
# [
#  ["Dom Casmurro", "Ana", 5],
#  ["1984", "Carlos", 12],
#  ["O Hobbit", "Marina", 3]
# ]
# O sistema precisa:
# 1. Listar apenas os livros que estão emprestados há mais de 7 dias.
# 2. Encontrar o livro emprestado há mais tempo.
# 3. Gerar uma lista apenas com os nomes dos usuários que têm livros emprestados.
# 4. Calcular a média de dias de empréstimo.



def biblioteca(lista_biblioteca):

    lista_emprestimo=[]
    lista_livros_emprestados =[]
    soma_dias=0
    livro_emprestado = lista_biblioteca[0]
    for i in lista_biblioteca:
        lista_emprestimo.append(i[1])
        soma_dias = soma_dias + i[2]
        if i[2] > livro_emprestado[2]:
            livro_emprestado = i
        if i[2] > 7:
            lista_livros_emprestados.append(i[0])
    true_livro_emprestado = livro_emprestado[0]
    media=soma_dias/(len(lista_biblioteca))

    resultado = [lista_livros_emprestados,true_livro_emprestado, lista_emprestimo, media]
    return resultado

lista_biblioteca=[["Dom Casmurro", "Ana", 5], ["1984", "Carlos", 12],["O Hobbit", "Marina", 3]]

fun = biblioteca(lista_biblioteca)

lista_livros_emprestados = fun[0]
true_livro_emprestado = fun[1]
lista_emprestimo = fun[2]
media = fun[3]





print(f"Os livros que estão emprestados a mais de 7 dias são {lista_livros_emprestados}\n O livro emprestado há mais tempo é o livro {true_livro_emprestado}\n Os usuários que tem livros emprestados são {lista_emprestimo}\n A média de dias emprestados é {media}")

