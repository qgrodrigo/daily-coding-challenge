Construir una Tabla Hash
En este laboratorio, construirás una tabla hash desde cero. Una tabla hash es una estructura de datos que almacena pares clave-valor. Una tabla hash funciona tomando la clave como entrada y luego aplicándole un hash de acuerdo con una función de hash específica.

Para el propósito de este laboratorio, la función de hash será simple: sumará los valores Unicode de cada carácter en la clave. El valor hash se utilizará entonces como la clave real para almacenar el valor asociado. El mismo valor hash también se utilizaría para recuperar y eliminar el valor asociado con la clave.

Objetivo: Cumplir con las historias de usuario a continuación y pasar todas las pruebas para completar el laboratorio.

Historias de usuario:

Deberías definir una clase llamada HashTable con un atributo collection inicializado a un diccionario vacío cuando se crea una nueva instancia de HashTable. El diccionario collection debería almacenar pares clave-valor basados en el valor hash de la clave.

La clase HashTable debería tener cuatro métodos de instancia: hash, add, remove y lookup.

El método hash debería:

Tomar una cadena como parámetro.
Devolver un valor hash calculado como la suma de los valores Unicode (ASCII) de cada carácter en la cadena. Puedes usar la función ord para este cálculo.
El método add debería:

Aceptar dos argumentos que representen un par clave-valor, y calcular el hash de la clave.
Usa el valor hash calculado como clave para almacenar un diccionario que contiene el par clave-valor dentro del diccionario collection.
Si varias claves producen el mismo valor hash, sus pares clave-valor deben almacenarse en el diccionario anidado existente bajo el mismo valor hash.
El método remove debería:

Tomar una clave como su argumento y calcular su hash.
Confirmar si la clave existe en collection.
Eliminar el par clave-valor correspondiente de la tabla hash.
Si la clave no existe en collection, no debería lanzar un error o eliminar nada.
El método lookup debería:

Tomar una clave como su argumento.
Calcular el hash de la clave y devolver el valor correspondiente almacenado dentro de la tabla hash.
Si la clave no existe en collection, debería devolver None.
Pruebas:
Aprobado:1. Deberías definir una clase HashTable.
Aprobado:2. Cuando se crea una nueva instancia de la clase HashTable, su atributo collection debería inicializarse a un diccionario vacío.
Aprobado:3. La clase HashTable debería tener un método hash.
Aprobado:4. El método hash debería tomar una cadena como parámetro.
Aprobado:5. El método hash debería tomar una cadena como su argumento y devolver la suma de los valores Unicode de cada carácter en la cadena.
Aprobado:6. La clase HashTable debería tener un método add.
Aprobado:7. El método add debería tomar una clave y un valor como parámetros.
Aprobado:8. La clase HashTable debería tener un método remove.
Aprobado:9. El método remove debería tomar una clave como parámetro.
Aprobado:10. Cuando intentas eliminar una clave que no existe en collection, no debería lanzar un error ni eliminar nada.
Aprobado:11. Si múltiples claves producen el mismo índice, el método remove debería eliminar solo el par clave-valor específico y no todo el diccionario en ese índice.
Aprobado:12. La clase HashTable debería tener un método lookup.
Aprobado:13. El método lookup debería tomar una clave como el parámetro.
Aprobado:14. HashTable().hash('golf') debería devolver 424.
Aprobado:15. HashTable().add('golf', 'sport') debería agregar el par clave-valor a la colección en la clave 424.
Aprobado:16. HashTable().add('dear', 'friend') y HashTable().add('read', 'book') deberían agregar ambos pares clave-valor a la colección en el índice 412 como un diccionario anidado.
Aprobado:17. Cuando una clave existe en la tabla hash, el método remove() debería eliminar la clave dada y su valor correspondiente de collection.
Aprobado:18. Cuando el par clave-valor 'golf', 'sport' existe en la tabla hash, HashTable().lookup('golf') debería devolver sport.
Aprobado:19. Cuando el par clave-valor 'golf', 'sport' no existe en la colección, HashTable().lookup('golf') debería devolver None.
Aprobado:20. Cuando la clave 'fcc' existe en la colección, HashTable().lookup('cfc') debería devolver None.
Aprobado:21. Cuando añades ('rose', 'flower') a la tabla hash, su atributo collection debería lucir así: { 441: { 'rose': 'flower' }}.
Aprobado:22. Cuando añades una clave que produce el mismo valor hash que una clave existente, como fcc y cfc, collection debería lucir así: { 300: { 'fcc': 'coding', 'cfc':  'chemical' }}.