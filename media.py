def calcular_media(numeros):
    total = sum(numeros)
    quantidade = len(numeros)
    media = total / quantidade
    return media

lista = [2, 4, 7, 8, 10]
media = calcular_media(lista)
print(media)

