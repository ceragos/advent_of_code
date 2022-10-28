# advent_of_code

--- Día 2: ¡Bucear! ---
Ahora, debes descubrir cómo pilotar esta cosa .

Parece que el submarino puede tomar una serie de comandos como forward 1, down 2 o up 3:

forward X aumenta la posición horizontal en X unidades.
down X aumenta la profundidad en X unidades.
up X disminuye la profundidad en X unidades.
Tenga en cuenta que ya que estás en un submarino, down y up afectan su profundidad , por lo que tienen el efecto contrario de lo que cabría esperar.

Parece que el submarino ya tiene un rumbo planificado (tu entrada del rompecabezas). Probablemente debería averiguar hacia dónde se dirige. Por ejemplo:

forward 5
down 5
forward 8
up 3
down 8
forward 2

Su posición horizontal y profundidad comienzan en 0. Los pasos anteriores los modificarían de la siguiente manera:

forward 5 agrega 5 a su posición horizontal, un total de 5.
down 5 agrega 5 a su profundidad, resultando en un valor de 5.
forward 8 agrega 8 a su posición horizontal, un total de 13.
up 3 disminuye la profundidad en 3, lo que da como resultado un valor de 2.
down 8 agrega 8 a su profundidad, resultando en un valor de 10.
forward 2 agrega 2 a su posición horizontal, un total de 15.
Después de seguir estas instrucciones, tendrá una posición horizontal 15 y una profundidad de 10. (Multiplicar estos juntos produce 150).

Calcula la posición horizontal y la profundidad que tendrías después de seguir el rumbo planificado. ¿Qué obtienes si multiplicas tu posición horizontal final por tu profundidad final?

--- La segunda parte ---
Según sus cálculos, el curso planeado no parece tener ningún sentido. Encuentra el manual del submarino y descubre que el proceso es en realidad un poco más complicado.

Además de la posición horizontal y la profundidad, también deberá realizar un seguimiento de un tercer valor, el objetivo , que también comienza en 0. Los comandos también significan algo completamente diferente de lo que pensaba al principio:

down X aumenta tu objetivo por X unidades.
up X disminuye tu objetivo por X unidades.
forward X hace dos cosas:
    Aumenta tu posición horizontal en X unidades.
    Aumenta tu profundidad en objetivo multiplicada por X.

Una vez más, tenga en cuenta que, dado que está en un submarino, down y up haga lo contrario de lo que podría esperar: "abajo" significa apuntar en la dirección positiva.

Ahora, el ejemplo anterior hace algo diferente:

forward 5 agrega 5 a su posición horizontal, un total de 5. Porque tu objetivo es 0, tu profundidad no cambia.
down 5 se suma 5 a su objetivo, lo que da como resultado un valor de 5.
forward 8 agrega 8 a su posición horizontal, un total de 13. Porque tu objetivo es 5, tu profundidad aumenta en 8 * 5 = 40.
up 3 disminuye su objetivo en 3, lo que da como resultado un valor de 2.
down 8 se suma 8 a su objetivo, lo que da como resultado un valor de 10.
forward 2 agrega 2 a su posición horizontal, un total de 15. Debido a que su objetivo es 10, su profundidad aumenta 2 * 10 = 20 hasta un total de 60.

Después de seguir estas nuevas instrucciones, tendrá una posición horizontal 15 y una profundidad de 60. (Multiplicar estos produce 900).

Con esta nueva interpretación de los comandos, calcule la posición horizontal y la profundidad que tendría después de seguir el rumbo planificado. ¿Qué obtienes si multiplicas tu posición horizontal final por tu profundidad final?