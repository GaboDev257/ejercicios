# Ejemplo de una lista en Python
# Las listas son colecciones ordenadas y mutables de elementos.
numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numbers)  # Imprimiendo contenido de la lista original.

numbers[0] = 111  #Modificando el primer elemento de la lista.
print("Nuevo contenido de la lista: ", numbers)  # Contenido de la lista actual.

numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("Nuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.

print(numbers[0]) # Accediendo al primer elemento de la lista.

#===========La función len()=============#
# La función len() devuelve la cantidad de elementos en una lista.
print("Cantidad de elementos en la lista:", len(numbers))  # Imprimiendo la cantidad de elementos en la lista.

#===========La instrucción del()=============#
# La instrucción del() elimina un elemento de la lista.
del numbers[0]  # Eliminando el primer elemento de la lista.
print("Contenido de la lista después de eliminar el primer elemento:", numbers)  # Imprimiendo el contenido de la lista después de eliminar el primer elemento.

#Los índices negativos son válidos
print("Último elemento de la lista:", numbers[-1])  # Imprimiendo el último elemento de la lista usando un índice negativo.
print("Penúltimo elemento de la lista:", numbers[-2])  # Imprimiendo el penúltimo elemento de la lista usando un índice negativo.

#===================Ejercicio===================#
hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.
print("La lista actual de números es: ", hat_list)
# Paso 1: escribe una línea de código que solicite al usuario
# reemplazar el número de en medio con un número entero ingresado por el usuario.
hat_list[2] = int(input("Ingresa un número: "))
print("La lista de números modificada es: ", hat_list)
# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
print("Eliminando un índice")
del hat_list[4]
print("La lista modificada es: ", hat_list)
# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print("La longitud final de la lista es de: ", len(hat_list), "elementos")


#===================MÉTODOS DE LISTAS===================#
# Las listas en Python tienen varios métodos útiles para manipular sus elementos.
# Aquí hay algunos ejemplos de métodos comunes de listas:

# append() - Agrega un elemento al final de la lista.
numbers.append(20)  # Agregando el número 20 al final de la lista
print("Lista después de append:", numbers)  # Imprimiendo la lista después de agregar un elemento.

# insert() - Inserta un elemento en una posición específica de la lista.
numbers.insert(1, 15)  # Insertando el número 15 en la segunda posición de la lista
print("Lista después de insert:", numbers)  # Imprimiendo la lista después de insertar un elemento.

#Puedes iniciar la vida de una lista creándola vacía (esto se hace con un par de corchetes vacíos) 
# y luego agregar nuevos elementos según sea necesario.

my_list = []  # Creando una lista vacía
# Agregando elementos a la lista vacía usando un bucle for.
# En este caso, agregamos los números del 1 al 5.
for i in range(5):
    my_list.append(i + 1)

print(my_list)
#El resultado será: [1, 2, 3, 4, 5]

my_list2 = []  # Creando una lista vacía.
# Agregando elementos al principio de la lista vacía usando un bucle for.
for i in range(5):
    my_list2.insert(0, i + 1)

print(my_list2)
#El resultado será: [5, 4, 3, 2, 1]