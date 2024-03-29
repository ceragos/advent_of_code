# advent_of_code
--- Día 3: Diagnóstico binario ---
El submarino ha estado haciendo algunos crujidos extraños, así que le pides que produzca un informe de diagnóstico por si acaso.

El informe de diagnóstico (su entrada del rompecabezas) consiste en una lista de números binarios que, cuando se decodifican correctamente, pueden decirle muchas cosas útiles sobre las condiciones del submarino. El primer parámetro a comprobar es el consumo de energía .

Debe usar los números binarios en el informe de diagnóstico para generar dos nuevos números binarios (llamados tasa gamma y tasa épsilon ). El consumo de energía se puede calcular multiplicando la tasa gamma por la tasa épsilon.

Cada bit de la velocidad gamma se puede determinar encontrando el bit más común en la posición correspondiente de todos los números en el informe de diagnóstico. Por ejemplo, dado el siguiente informe de diagnóstico:

00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010

Considerando solo el primer bit de cada número, hay cinco 0 bits y siete 1 bits. Dado que el bit más común es 1, el primer bit de la tasa de gamma es 1.

El segundo bit más común de los números en el informe de diagnóstico es 0, por lo que el segundo bit de la tasa de gamma es 0.

El valor más común de la tercera, cuarta, y quinta bits son 1, 1, y 0, respectivamente, y por lo que los tres últimos bits de la tasa de gamma son 110.

Entonces, la tasa gamma es el número binario 10110 o 22 en decimal.

La tasa de épsilon se calcula de manera similar; en lugar de usar el bit más común, se usa el bit menos común de cada posición. Entonces, la tasa de épsilon es 01001, o 9 en decimal. Multiplicando la tasa gamma (22) por el tipo epsilon (9) produce el consumo de energía, 198.

Utilice los números binarios en su informe de diagnóstico para calcular la tasa gamma y la tasa épsilon, luego multiplíquelos. ¿Cuál es el consumo de energía del submarino? (Asegúrese de representar su respuesta en decimal, no en binario).

--- La segunda parte ---
A continuación, debe verificar la clasificación de soporte vital, que se puede determinar multiplicando la clasificación del generador de oxígeno por la clasificación del depurador de CO2.

Tanto la clasificación del generador de oxígeno como la clasificación del depurador de CO2 son valores que se pueden encontrar en su informe de diagnóstico; encontrarlos es la parte difícil. Ambos valores se ubican mediante un proceso similar que implica filtrar valores hasta que solo queda uno. Antes de buscar cualquiera de los valores de calificación, comience con la lista completa de números binarios de su informe de diagnóstico y considere solo el primer bit de esos números. Entonces:

Mantenga solo los números seleccionados por los criterios de bit para el tipo de valor de clasificación que está buscando. Descarte los números que no coincidan con los criterios de bits.
Si solo le queda un número, deténgase; este es el valor de clasificación que está buscando.
De lo contrario, repita el proceso, considerando el siguiente bit a la derecha.
Los criterios de bits dependen del tipo de valor de clasificación que desee encontrar:

Para encontrar la clasificación del generador de oxígeno , determine el valor más común (0 o 1) en la posición actual del bit y mantenga solo los números con ese bit en esa posición. Si 0 y 1 son igualmente comunes, mantenga los valores con a 1 en la posición que se está considerando.
Para encontrar la clasificación del depurador de CO2 , determine el valor menos común (0 o 1) en la posición actual del bit y mantenga solo los números con ese bit en esa posición. Si 0 y 1 son igualmente comunes, mantenga los valores con a 0 en la posición que se está considerando.
Por ejemplo, para determinar el valor nominal del generador de oxígeno utilizando el mismo informe de diagnóstico de ejemplo anterior:

Comience con los 12 números y considere solo el primer bit de cada número. Hay más 1 bits (7) que los 0 bits (5), a fin de mantener sólo los 7 números con una 1 en la primera posición: 11110, 10110, 10111, 10101, 11100, 10000, y 11001.
Luego, consideremos el segundo bit de los 7 números restantes: hay más 0 bits (4) que los 1 bits (3), a fin de mantener sólo los 4 números con una 0 en la segunda posición: 10110, 10111, 10101, y 10000.
En la tercera posición, tres de los cuatro números tienen una 1, a fin de mantener los tres: 10110, 10111, y 10101.
En la cuarta posición, dos de los tres números tienen una 1, así que mantén esos dos: 10110 y 10111.
En la quinta posición, hay un número igual de 0 bits y 1 bits (uno cada uno). Por lo tanto, para encontrar la calificación generador de oxígeno , mantener el número con una 1 en esa posición: 10111.
Como solo queda un número, deténgase; la clasificación del generador de oxígeno es 10111, o 23 en decimal.
Luego, para determinar el valor de clasificación del depurador de CO2 del mismo ejemplo anterior:

Comience de nuevo con los 12 números y considere solo el primer bit de cada número. Hay menos 0 bits (5) que 1 los bits (7), a fin de mantener sólo los 5 números con una 0 en la primera posición: 00100, 01111, 00111, 00010, y 01010.
Luego, considere el segundo bit de los 5 números restantes: hay menos 1 bits (2) que 0 bits (3), así que mantenga solo los 2 números con a 1 en la segunda posición: 01111y 01010.
En la tercera posición, hay un número igual de 0 bits y 1 bits (uno cada uno). Por lo tanto, para encontrar la calificación depurador de CO2 , mantener el número con una 0 en esa posición: 01010.
Como solo queda un número, deténgase; la clasificación del depurador de CO2 es 01010, o 10 en decimal.
Finalmente, para encontrar la clasificación de soporte vital, multiplique la clasificación del generador de oxígeno (23) por la clasificación del depurador de CO2 (10) para obtener 230.

Utilice los números binarios en su informe de diagnóstico para calcular la clasificación del generador de oxígeno y la clasificación del depurador de CO2, luego multiplíquelos. ¿Cuál es la clasificación de soporte vital del submarino? (Asegúrese de representar su respuesta en decimal, no en binario).