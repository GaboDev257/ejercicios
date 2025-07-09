# Listas
#Son colecciones ordenadas y modificables. Permiten elementos duplicados.
# Son útiles para almacenar secuencias de elementos.

frutas = ["manzana, banano, pera, ciruela"]
frutas.append("naranja")  # Agregar un elemento
frutas.remove("pera")  # Eliminar un elemento 
print(frutas)  # Imprimir la lista actualizada
print(frutas[0])  # Acceder al primer elemento

# Tuplas
#Son colecciones ordenadas, pero inmutables (no se pueden modificar después de ser creadas).
# Son útiles para almacenar datos que no deben cambiar, como coordenadas o fechas.

coordenadas = (10.0, 20.0)  # Definir una tupla
print(coordenadas)  # Imprimir la tupla 
print(coordenadas[0])  # Acceder al primer elemento de la tupla

#Diccionarios (dict)
#Son colecciones no ordenadas (en versiones antiguas), con pares clave:valor. Son modificables y no permiten claves duplicadas.
# Son útiles para almacenar datos relacionados, como información de contacto o configuraciones.

contacto = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}  # Definir un diccionario
print(contacto)  # Imprimir el diccionario
print(contacto["nombre"])  # Acceder al valor asociado a la clave "nombre"

# Conjuntos (set)
#Son colecciones no ordenadas y no indexadas, que no permiten elementos duplicados.
# Son útiles para almacenar elementos únicos, como etiquetas o categorías.

colores = {"rojo", "verde", "azul"}  # Definir un conjunto
print(colores)  # Imprimir el conjunto
colores.add("amarillo")  # Agregar un elemento al conjunto
print(colores)  # Imprimir el conjunto actualizado

