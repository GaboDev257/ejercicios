print("Bienvenido a la cafetería") 
print("Menú:") 
print("1. Café - $4.000") 
print("2. Té - $3.000") 
print("3. Chocolate - $4.500") 
opcion = input("Seleccione una opción (1-3): ") 
 
if opcion == "1": 
    print("Has elegido Café. Precio: $4.000") 
elif opcion == "2": 
    print("Has elegido Té. Precio: $3.000") 
elif opcion == "3": 
    print("Has elegido Chocolate. Precio: $4.500") 
else: 
    print("Opción no válida. Por favor, selecciona una bebida del menú.") 