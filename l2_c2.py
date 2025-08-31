# 1. Receba as distâncias percorridas em 6 viagens e armazene em uma lista.
# 2. Calcule a distância total percorrida.
# 3. Mostre a maior e a menor distância.
# 4. Calcule a média das distâncias arredondada para cima (use math.ceil).
import math


def distancias_fun(distancias):


    distancias.sort()
    menor_distancia = distancias[0]
    maior_distancia = distancias[5]

    media_distancias = soma /6

    media_arredondada = math.ceil(media_distancias)

    resultado = [maior_distancia,menor_distancia,media_arredondada]

soma=0
distancias=[]
for i in range (6):
    d=float(input('Digite a distância em km:'))
    soma = soma + d
    distancias.append(d)



fun = distancias_fun(distancias)
maior_distancia = fun[0]
menor_distancia = fun[1]
media_arredondada = fun[3]

print(f"A maior distância foi {maior_distancia}km e a menor distância foi {menor_distancia}km. A média das distâncias arrendodadas para cima é {media_arredondada}")

