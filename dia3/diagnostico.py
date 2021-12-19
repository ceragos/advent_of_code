informe = []
with open('dia3/input.txt', 'r') as archivo:
    for linea in archivo:
        binario = [*linea]
        binario.pop()
        informe.append(binario)

def binario_a_decimal(binario):
    potencias = []
    for indice, valor in enumerate([*binario]):
        potencias.append(2**indice)
    # Se debe invertir la lista de potencias
    potencias = list(reversed(potencias))
    
    valores = []
    for indice, potencia in enumerate(potencias):
        valores.append(int(binario[indice]) * potencia)
    valor_decimal = sum(valores)
    return valor_decimal

def consumo_energia(informe):
    bit_posicion = []
    # Se crea una lista con la cantidad de posiciones que tiene el primer arreglo del informe.
    for i in range(len(informe[0])):
        bit_posicion.append([])
    
    for binario in informe:
        for indice, bit in enumerate(binario):
            bit_posicion[indice].append(bit)
    
    tasa_gamma = []
    tasa_epsilon = []
    for lista in bit_posicion:
        if lista.count('0') > lista.count('1'):
            tasa_gamma.append('0')
            tasa_epsilon.append('1')
        else:
            tasa_gamma.append('1')
            tasa_epsilon.append('0')
    tasa_gamma = "".join(tasa_gamma)
    tasa_epsilon = "".join(tasa_epsilon)

    tasa_gamma_decimal = binario_a_decimal(tasa_gamma)
    tasa_epsilon_decimal = binario_a_decimal(tasa_epsilon)
    consumo_energia = tasa_gamma_decimal * tasa_epsilon_decimal
    return consumo_energia

print(consumo_energia(informe))
