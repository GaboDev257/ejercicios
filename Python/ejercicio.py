'''
def permisoEntrada (edad, sexo): 
    if (edad <= 20 and sexo == "F"):
        print("No es admitida")
    elif (edad < 18 and sexo == "M"):
       print("No es admitido")
    else: 
        print("Bienvenid@")   

permisoEntrada(19, "F")

'''
#Definimos variables
edad = int(input("Ingresa tu edad:")) #int
altura = 1.68 #float
nombre = "Gabriel" #str
es_estudiante = True #bool

#Realizamos operaciones
suma = edad + 5
division = altura / 2
multiplicacion = edad * 2
modulo = edad % 4

#Convertimos tipos de datos
altura_entero = int(altura)
edad_float = float(edad)

#Imprimimmos resultados
print(edad)
print(altura)
print(nombre)
print(es_estudiante)
print(suma)
print(division)
print(multiplicacion)
print(modulo)
print(altura_entero)
print(edad_float)


if (edad < 18):
    print("El usuario es menor de edad")
else:
    print("El usuario es mayor de edad")    