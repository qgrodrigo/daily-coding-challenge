Construye una Interfaz de Player
Objetivo: Cumplir con las historias de usuario a continuación y pasar todas las pruebas para completar el laboratorio.

Historias de usuario:

Debes definir una clase abstracta llamada Player que herede de la clase abc.ABC.

La clase Player debe tener un método __init__ que establezca:

El atributo moves a una lista vacía.
El atributo position a (0, 0).
El atributo path a una lista que contiene la posición inicial.
La clase Player debe tener un método llamado make_move que:

Usa random.choice para obtener un movimiento aleatorio del atributo moves (definido en la clase concreta).
Suma los valores del movimiento seleccionado a la posición actual y actualiza el atributo position.
Agrega la nueva tupla position al atributo path.
Devuelve la nueva position.
La clase Player debe tener un método abstracto llamado level_up que debe ser implementado en clases concretas.

Debes definir una clase Pawn que herede de la clase Player.

La clase Pawn debe usar super() para llamar al método __init__ del padre y luego establecer el atributo moves como una lista de tuplas que representan las coordenadas x, y.

Cada tupla de coordenadas debe representar un movimiento de 1 unidad en las siguientes direcciones: arriba, abajo, izquierda, derecha.

La clase Pawn debe implementar un método concreto level_up agregando más movimientos al atributo moves. Los movimientos añadidos deben representar los cuatro movimientos diagonales (por ejemplo, 1 unidad hacia abajo más 1 unidad hacia la izquierda).

Nota: Los módulos de la biblioteca estándar deben importarse sin usar alias. Las pruebas relacionadas con la clase Player fallarán hasta que la clase Pawn pueda ser instanciada.

Pruebas:
Aprobado:1. Debes tener una clase llamada Player.
Aprobado:2. La clase Player debe heredar de la clase ABC del módulo abc.
Aprobado:3. La clase Player debe tener un método __init__.
Aprobado:4. El método __init__ de Player debe tener un solo parámetro self.
Aprobado:5. El método __init__ de Player debe establecer self.moves como una lista vacía.
Aprobado:6. El método __init__ de Player debe establecer self.position en (0, 0).
Aprobado:7. El método __init__ de Player debe establecer self.path como una lista que contenga la posición inicial.
Aprobado:8. La clase Player debe tener un método make_move.
Aprobado:9. El método make_move del Player debe tener un solo parámetro self.
Aprobado:10. El método make_move del Player debe usar random.choice para obtener un movimiento aleatorio del atributo moves.
Aprobado:11. El método make_move del Player debería actualizar el atributo position sumándole las coordenadas del movimiento seleccionado aleatoriamente.
Aprobado:12. El método make_move del Player debe agregar la nueva tupla position al atributo path.
Aprobado:13. El método make_move del Player debería devolver el atributo position actualizado.
Aprobado:14. La clase Player debe tener un método level_up.
Aprobado:15. El método level_up de Player debe tener un solo parámetro self.
Aprobado:16. El método level_up del Player debería ser un método abstracto.
Aprobado:17. La clase Player debería ser una clase abstracta.
Aprobado:18. Debes tener una clase llamada Pawn.
Aprobado:19. La clase Pawn debe heredar de la clase Player.
Aprobado:20. La clase Pawn debe tener un método __init__.
Aprobado:21. El método __init__ de Pawn debe tener un solo parámetro self.
Aprobado:22. El método __init__ de Pawn debe llamar al __init__ del padre usando la función super.
Aprobado:23. El método __init__ de Pawn debe establecer el atributo moves como una lista de tuplas que representan coordenadas x, y, donde cada tupla de coordenadas representa un movimiento de 1 unidad en las siguientes direcciones: arriba, abajo, izquierda, derecha.
Aprobado:24. La clase Pawn debe tener un método level_up.
Aprobado:25. El método level_up de Pawn debería agregar el movimiento diagonal de 1 unidad a cada uno de los cuatro lados al atributo moves.