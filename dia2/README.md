# advent_of_code

--- Día 2: ¡Bucear! ---
Ahora, debes descubrir cómo pilotar esta cosa .

Parece que el submarino puede tomar una serie de comandos como forward 1, down 2o up 3:

forward Xaumenta la posición horizontal en Xunidades.
down X aumenta la profundidad en Xunidades.
up X disminuye la profundidad en Xunidades.
Tenga en cuenta que ya que estás en un submarino, downy upafectan su profundidad , por lo que tienen el efecto contrario de lo que cabría esperar.

Parece que el submarino ya tiene un rumbo planificado (tu entrada del rompecabezas). Probablemente debería averiguar hacia dónde se dirige. Por ejemplo:

forward 5
down 5
forward 8
up 3
down 8
forward 2

Su posición horizontal y profundidad comienzan en 0. Los pasos anteriores los modificarían de la siguiente manera:

forward 5agrega 5a su posición horizontal, un total de 5.
down 5agrega 5a su profundidad, resultando en un valor de 5.
forward 8agrega 8a su posición horizontal, un total de 13.
up 3disminuye la profundidad en 3, lo que da como resultado un valor de 2.
down 8agrega 8a su profundidad, resultando en un valor de 10.
forward 2agrega 2a su posición horizontal, un total de 15.
Después de seguir estas instrucciones, tendrá una posición horizontal 15y una profundidad de 10. (Multiplicar estos juntos produce 150).

Calcula la posición horizontal y la profundidad que tendrías después de seguir el rumbo planificado. ¿Qué obtienes si multiplicas tu posición horizontal final por tu profundidad final?
