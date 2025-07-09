estudiantes = [] 
while True: 
    nombre = input("Nombre: ") 
    edad = int(input("Edad: ")) 
    curso = input("Curso: ") 
    estudiantes.append({"nombre": nombre, "edad": edad, "curso": curso}) 
    continuar = input("¿Deseas agregar otro estudiante? (s/n): ") 
    if continuar.lower() != 's': 
        break 
print("\nListado de estudiantes:") 
for est in estudiantes: 
    print(est) 