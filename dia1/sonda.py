# Parte 1
informe_sonda = []
with open("dia1/input.txt","r") as archivo:
    for linea in archivo:
        informe_sonda.append(int(linea))

def contador_informe_sonda(informe_sonda, nombre_informe):
    contador_registro_incremental = 0
    contador_registro_decremental = 0
    registro_anterior = informe_sonda[0]

    for registro in informe_sonda[1:]:
        if registro > registro_anterior:
            contador_registro_incremental += 1
        else:
            contador_registro_decremental += 1
        registro_anterior = registro

    print("¿Cuántas {1}s son más grandes que la {1} anterior? {0}".format(contador_registro_incremental, nombre_informe))
    print("¿Cuántas {1}as son más pequeñas que la {1} anterior? {0}".format(contador_registro_decremental, nombre_informe))

contador_informe_sonda(informe_sonda, "medida")

# Parte 2
ventanas = []
limite_ventanas = len(informe_sonda) - 3

for iteracion in range(len(informe_sonda)):
    if iteracion > limite_ventanas:
        break
    ventanas.append(sum(informe_sonda[iteracion:iteracion+3]))

contador_informe_sonda(ventanas, "ventana")
