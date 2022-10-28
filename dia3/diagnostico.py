from time import sleep


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

class SoporteVital():
    contador_ceros = 0
    contador_unos = 0
    unos = []
    ceros = []

    def __init__(self, informe):
        self.informe = informe
        generador_oxigeno = self.clasificar_generador_oxigeno()
        depurador_CO2 = self.clasificar_depurador_CO2()
        self.clasificacion = binario_a_decimal(''.join(generador_oxigeno)) * binario_a_decimal(''.join(depurador_CO2))

    def clasificar_generador_oxigeno(self):
        proximo_recorrido = self.informe

        for i in range(len(self.informe[0])):
            self.contador_ceros = 0
            self.contador_unos = 0
            self.unos = []
            self.ceros = []

            for binario in proximo_recorrido:
                if binario[i] == '0':
                    self.contador_ceros = self.contador_ceros + 1
                    self.ceros.append(binario)
                else:
                    self.contador_unos = self.contador_unos + 1
                    self.unos.append(binario)

            if self.contador_unos >= self.contador_ceros:
                proximo_recorrido = self.unos
            else:
                proximo_recorrido = self.ceros

            if len(proximo_recorrido) == 1:
                binario = proximo_recorrido[0]
                return binario

    def clasificar_depurador_CO2(self):
        proximo_recorrido = self.informe

        for i in range(len(self.informe[0])):
            self.contador_ceros = 0
            self.contador_unos = 0
            self.unos = []
            self.ceros = []

            for binario in proximo_recorrido:
                if binario[i] == '0':
                    self.contador_ceros = self.contador_ceros + 1
                    self.ceros.append(binario)
                else:
                    self.contador_unos = self.contador_unos + 1
                    self.unos.append(binario)

            if self.contador_unos < self.contador_ceros:
                proximo_recorrido = self.unos
            else:
                proximo_recorrido = self.ceros

            if len(proximo_recorrido) == 1:
                binario = proximo_recorrido[0]
                return binario

print(consumo_energia(informe))

soporte_vital = SoporteVital(informe)
print(soporte_vital.clasificacion)
