medidas = []
with open("dia1/input.txt","r") as archivo:
    for linea in archivo:
        medidas.append(int(linea))

def contador_submarino(lista, nombre):
    medida_anterior = lista[0]
    contador_medida_incremental = 0
    contador_medida_decremental = 0

    for item in lista[1:]:
        if item > medida_anterior:
            contador_medida_incremental += 1
        else:
            contador_medida_decremental += 1
        medida_anterior = item

    print("¿Cuántas {1}s son más grandes que la {1} anterior? {0}".format(contador_medida_incremental, nombre))
    print("¿Cuántas {1}as son más pequeñas que la {1} anterior? {0}".format(contador_medida_decremental, nombre))

contador_submarino(medidas, "medida")
