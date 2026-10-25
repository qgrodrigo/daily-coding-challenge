Construye un Rastreador de Estadísticas de Personajes de Juego
En este laboratorio, construirás un rastreador de estadísticas de personajes de juego. El programa te permitirá crear un personaje con atributos específicos, actualizar esos atributos y obtener las estadísticas actuales del personaje.

Objetivo: Cumplir con las historias de usuario a continuación y pasar todas las pruebas para completar el laboratorio.

Historias de usuario:

Crea una clase llamada GameCharacter que representa un personaje del juego y gestiona las estadísticas del personaje.

Al instanciarse, un nuevo objeto GameCharacter debe tener los siguientes atributos:

_name establecido con la cadena dada en el momento de la instanciación.
_health establecido en 100.
_mana establecido en 50.
_level establecido en 1.
Crea una propiedad name para acceso de solo lectura al nombre del personaje.

Para la propiedad health:

Define un getter que devuelve la salud actual.
Define un setter que impida que la salud se establezca por debajo de 0 y limite la salud a 100.
Para la propiedad mana:

Define un getter que devuelva el mana actual.
Define un setter que impida que el mana se establezca por debajo de 0 y limite el mana a 50.
Crea un getter para level que devuelva el nivel actual del personaje.

Define un método llamado level_up que:

Aumenta el nivel del personaje en 1.
Restablece la salud a 100 y el mana a 50 usando sus correspondientes setters de propiedad.
Imprime un mensaje en la forma <name> leveled up to <level>! (donde <name> y <level> deben ser reemplazados por el nombre del personaje y el nuevo nivel, respectivamente).
Define un método __str__ que devuelva una cadena formateada que incluya:

El nombre del personaje.
El nivel del personaje.
La salud actual del personaje.
El mana actual del personaje.
Por ejemplo, un personaje llamado Kratos, justo después de la instanciación, debería representarse como lo siguiente:

Name: Kratos
Level: 1
Health: 100
Mana: 50
Ejemplo de uso
Código de ejemplo
hero = GameCharacter('Kratos') # Creates a new character named Kratos
print(hero)  # Displays the character's stats

hero.health -= 30  # Decreases health by 30
hero.mana -= 10    # Decreases mana by 10
print(hero)  # Displays the updated stats

hero.level_up()  # Levels up the character
print(hero)  # Displays the stats after leveling up
Pruebas:
Aprobado:1. Debes tener una clase GameCharacter.
Aprobado:2. Debes tener un método __init__ en la clase GameCharacter.
Aprobado:3. El método __init__ debe tener dos parámetros, siendo el primero self.
Aprobado:4. Debes asignar self._name a la cadena dada en el momento de la instanciación dentro del método __init__.
Aprobado:5. Debes asignar 100 a self._health dentro del método __init__.
Aprobado:6. Debes asignar 50 a self._mana dentro del método __init__.
Aprobado:7. Debes asignar 1 a self._level dentro del método __init__.
Aprobado:8. Debes tener un método name en la clase GameCharacter.
Aprobado:9. El método name debe tener solo un parámetro, self.
Aprobado:10. Debes retornar self._name en el método name.
Aprobado:11. El método name debe tener un decorador @property.
Aprobado:12. Debes tener un método health en la clase GameCharacter.
Aprobado:13. El método health debe tener solo un parámetro, self.
Aprobado:14. Debes retornar self._health en el método health.
Aprobado:15. El método health debe tener un decorador @property.
Aprobado:16. Debes crear un método setter health.
Aprobado:17. El método setter de health debe tener un decorador @health.setter.
Aprobado:18. El método setter health debe tener dos parámetros, siendo el primero self.
Aprobado:19. Debes establecer self._health en 0 si el valor dado al setter health es menor que 0.
Aprobado:20. Debes establecer self._health en 100 si el valor dado al setter health es mayor que 100.
Aprobado:21. Debes establecer self._health al valor dado al setter health cuando el valor esté entre 0 y 100.
Aprobado:22. Deberías tener un método mana en la clase GameCharacter.
Aprobado:23. El método mana debe tener solo un parámetro, self.
Aprobado:24. Debes retornar self._mana en el método mana.
Aprobado:25. El método mana debe tener un decorador @property.
Aprobado:26. Debes crear un método setter mana.
Aprobado:27. El método setter de mana debe tener un decorador @mana.setter.
Aprobado:28. El método setter mana debe tener dos parámetros, siendo el primero self.
Aprobado:29. Debes establecer self._mana en 0 si el valor dado al setter mana es menor que 0.
Aprobado:30. Debes establecer self._mana en 50 si el valor dado al setter mana es mayor que 50.
Aprobado:31. Debes asignar self._mana al valor dado al setter mana si el valor está entre 0 y 50.
Aprobado:32. Deberías tener un método level en la clase GameCharacter.
Aprobado:33. El método level debe tener solo un parámetro, self.
Aprobado:34. Debes retornar self._level en el método level.
Aprobado:35. El método level debe tener un decorador @property.
Aprobado:36. Deberías tener un método level_up en la clase GameCharacter.
Aprobado:37. El método level_up debe tener solo un parámetro, self.
Aprobado:38. Debes aumentar self._level en 1 en el método level_up.
Aprobado:39. Debes establecer self.health en 100 en el método level_up.
Aprobado:40. Debes establecer self.mana en 50 en el método level_up.
Aprobado:41. El método level_up debería imprimir <name> leveled up to <level>! (donde <name> y <level> deben ser reemplazados por el nombre del personaje y el nuevo nivel, respectivamente).
Aprobado:42. Debes tener un método __str__ en la clase GameCharacter.
Aprobado:43. El método __str__ debe tener solo un parámetro, self.
Aprobado:44. Tu método __str__ debe devolver una cadena con las estadísticas del personaje usando el formato proporcionado.