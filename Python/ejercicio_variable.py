def cargar_vector(tamano=10):
   vector = []
   print(f"Ingrese {tamano} números:")
   for i in range(tamano):
       num = int(input(f"Número {i + 1}: "))
       vector.append(num)
   return vector
 
def burbuja(lista):
   n = len(lista)
   for i in range(n):
       for j in range(0, n - i - 1):
           if lista[j] > lista[j + 1]:
              lista[j], lista[j + 1] = lista[j + 1], lista[j]
   return lista
 
def seleccion(lista):
   n = len(lista)
   for i in range(n):
       min_index = i
       for j in range(i + 1, n):
           if lista[j] < lista[min_index]:
              min_index = j
       lista[i], lista[min_index] = lista[min_index], lista[i]
   return lista
 
# Programa principal
vector_original = cargar_vector()
 
# Copias para no modificar el original
vector_burbuja = vector_original.copy()
vector_seleccion = vector_original.copy()
 
# Ordenamientos
ordenado_burbuja = burbuja(vector_burbuja)
ordenado_seleccion = seleccion(vector_seleccion)
 
# Resultados
print("\nVector original:", vector_original)
print("Ordenado por burbuja:", ordenado_burbuja)
print("Ordenado por selección:", ordenado_seleccion)