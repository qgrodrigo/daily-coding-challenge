onstruir un personaje de RPG
En este laboratorio, practicarás los fundamentos de Python construyendo una pequeña aplicación que crea un personaje para una aventura RPG.

Objetivo: Cumplir con las historias de usuario a continuación y pasar todas las pruebas para completar el laboratorio.

Historias de usuario:

Debes tener una función llamada create_character.
La función debe aceptar, en orden, un nombre de personaje seguido por tres estadísticas: fuerza, inteligencia y carisma.
Se debe validar el nombre del personaje:
Si el nombre del personaje no es una cadena, la función debe devolver The character name should be a string.
Si el nombre del personaje es una cadena vacía, la función debe devolver The character should have a name.
Si el nombre del personaje tiene más de 10 caracteres, la función debe devolver The character name is too long.
Si el nombre del personaje contiene espacios, la función debe devolver The character name should not contain spaces.
Las estadísticas también deben ser validadas:
Si una o más estadísticas no son enteros, la función debe devolver All stats should be integers.
Si una o más estadísticas son menores que 1, la función debe devolver All stats should be no less than 1.
Si una o más estadísticas son mayores que 4, la función debe devolver All stats should be no more than 4.
Si la suma de todas las estadísticas es diferente de 7, la función debe devolver The character should start with 7 points.
Si todos los valores pasan la verificación, la función debe devolver una cadena con cuatro líneas:
la primera línea debe contener el nombre del personaje
las líneas 2-4 deben comenzar con la abreviatura de la estadística, STR, INT o CHA (en ese orden), luego un espacio, y luego un número de puntos llenos (●) igual al valor de la estadística, y un número de puntos vacíos (○) para llegar a 10. Ejemplo: si el valor de fuerza es 3 debe haber 3 puntos llenos seguidos de 7 puntos vacíos. Los puntos se dan en el editor.
Aquí está la cadena que debe ser devuelta por create_character('ren', 4, 2, 1):

ren
STR ●●●●○○○○○○
INT ●●○○○○○○○○
CHA ●○○○○○○○○○
NOTA: aunque str e int son abreviaturas comunes para las estadísticas, recuerda que son palabras clave reservadas en Python y no deben usarse como nombres de variables.

Pruebas:
Esperando:1. Debes tener una función llamada create_character.
Esperando:2. Cuando create_character se llama con un primer argumento que no es una cadena, debería devolver The character name should be a string.
Esperando:3. Cuando se llama a create_character con un primer argumento que es una cadena, no debe devolver The character name should be a string.
Esperando:4. Cuando create_character se llama con un primer argumento que es una cadena vacía, debería devolver The character should have a name.
Esperando:5. Cuando se llama a create_character con un primer argumento que no es una cadena vacía, no debe devolver The character should have a name.
Esperando:6. Cuando create_character se llama con un primer argumento que tiene más de 10 caracteres, debería devolver The character name is too long.
Esperando:7. La función create_character no debería decir que el carácter es demasiado largo cuando no tiene más de 10 caracteres.
Esperando:8. Cuando create_character se llama con un primer argumento que contiene un espacio debería devolver The character name should not contain spaces.
Esperando:9. Cuando se llama a create_character con un primer argumento que no contiene un espacio, no debe devolver The character name should not contain spaces.
Esperando:10. Cuando create_character se llama con un segundo, tercer o cuarto argumento que no es un entero, debería devolver All stats should be integers.
Esperando:11. Cuando create_character se llama con un segundo, tercer y cuarto argumento que son todos enteros, no debe devolver All stats should be integers.
Esperando:12. Cuando create_character se llama con un segundo, tercer o cuarto argumento que sea menor que 1, debería devolver All stats should be no less than 1.
Esperando:13. Cuando se llama a create_character con un segundo, tercer y cuarto argumento que no sean menores que 1, no debe devolver All stats should be no less than 1.
Esperando:14. Cuando create_character se llama con un segundo, tercer o cuarto argumento que sea mayor que 4, debería devolver All stats should be no more than 4.
Esperando:15. Cuando se llama a create_character con un segundo, tercer y cuarto argumento que no sean mayores que 4, no debe devolver All stats should be no more than 4.
Esperando:16. Cuando create_character se llama con un segundo, tercer o cuarto argumento que no suma 7, debería devolver The character should start with 7 points.
Esperando:17. Cuando se llama a create_character con un segundo, tercer y cuarto argumento que suman 7 no debe devolver The character should start with 7 points.
Esperando:18. create_character('ren', 4, 2, 1) debería devolver ren\nSTR ●●●●○○○○○○\nINT ●●○○○○○○○○\nCHA ●○○○○○○○○○.
Esperando:19. Cuando create_character se llama con valores válidos debería mostrar las estadísticas del personaje como se requiere.