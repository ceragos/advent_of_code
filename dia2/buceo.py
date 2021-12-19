comandos = []
with open('dia2/input.txt', 'r') as archivo:
    for linea in archivo:
        comandos.append(linea)

def ubicacion(comandos):
    posicion_horizontal = 0
    profundidad = 0

    for instruccion in comandos:
        controles, unidad = instruccion.split()
        unidad = int(unidad)
        if controles == 'forward':
            posicion_horizontal += unidad
        elif controles == 'up':
            profundidad -= unidad
        elif controles == 'down':
            profundidad += unidad
    ubicacion = posicion_horizontal * profundidad
    print('Su ubicación actual es: {}'.format(ubicacion))

def ubicacion_objetivo(comandos):
    posicion_horizontal = 0
    profundidad = 0
    objetivo = 0

    for instruccion in comandos:
        controles, unidad = instruccion.split()
        unidad = int(unidad)
        if controles == 'forward':
            posicion_horizontal += unidad
            profundidad += objetivo * unidad
        elif controles == 'up':
            objetivo -= unidad
        elif controles == 'down':
            objetivo += unidad
    ubicacion = posicion_horizontal * profundidad
    print('Su ubicación actual es: {}'.format(ubicacion))

ubicacion(comandos)
ubicacion_objetivo(comandos)