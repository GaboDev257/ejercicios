#Tabla de multiplicar 
#Se usarán ciclos para realizar los respectivos procesos

numero = int(input("ingrese el numero a multiplicar"))
multiplicacion = 0
 
print("dependiendo de la opcion del 1 al 3 elija:")
print("1 - for")
print("2 - while")
print("3 - do while")
 
opcion = int(input(""))
 
match opcion:
    case 1:
        for i in range(1,11):
            multiplicacion = i * numero
            print(numero, "*", i , "=", multiplicacion)
           
    case 2:
        i = 1
        while i <= 10:
            multiplicacion = i*numero
            print(numero, "*", i , "=", multiplicacion)
            i = i+1
    

def factorial():
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado
 
print("Ejercicio de funciones")
numero = int(input("Ingrese un numero: "))
if numero < 0:
    raise ValueError("El numero no puede ser negativo")
else:
    print(factorial())