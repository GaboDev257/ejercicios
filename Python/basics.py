#This is a basic comment
""""This is a multi-line comment"""
print("Hola estudiantes")

#Solicitar el nombre del usuario o un dato en específico
nombre = input("Ingrese su nombre: ")
# Imprimir un mensaje de bienvenida de una forma
# La f -string permite insertar variables directamente en la cadena
print(f"Hola {nombre}, bienvenido al curso de Python")

# Imprimir un mensaje de bienvenida de otra forma
print("Hola", nombre,", bienvenido al curso de Python")


#Condiciones simples
mi_numero = int(input("Ingrese un número: ")) #int convierte el input a un número entero    

if mi_numero < 5 and mi_numero % 2 == 0:
    print("Este número es menor que 5 y es par")
else:
    print("Este número es mayor o igual que 5")
    

#Condicion Compuesta
mi_edad = int(input("Ingrese su edad: "))

if mi_edad < 18:
    print("Eres menor de edad, no tienes acceso al sitio")
elif mi_edad > 65:
    print("Sobrepasas la edad máxima, no puedes ingresar al sitio")
else:
    print("Bienvenido al sitio, puedes ingresar")    


entrada = input("Ingresa la planta: ")

if entrada == "ESPATIFILIO":
    print("Sí, ¡El ESPATIFILIO! es la mejor planta de todos los tiempos!")
elif entrada == "espatifilo":
    print("No, ¡quiero un gran ESPATIFILIO!")
else:
    print(f'¡ESPATIFILIO!, ¡No {entrada}!')
    
        
#Condiciones anidadas
mi_numero = int(input("Ingrese un número: "))   
if mi_numero < 10:
    print("El número es menor que 10")
    if mi_numero % 2 == 0:
        print("El número es par")
        
    else:
        print("El número es impar")
else: 
    print("El número es mayor o igual que 10")
    if mi_numero % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")
        
#Ejercicios simples para practicar operadores 

# Conversión de millas a kilómetros y viceversa
# 1 milla = 1.61 kilómetros 
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61


print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")

# Conversión de grados Celsius a Fahrenheit y viceversa
# Fórmula: F = C * 9/5 + 32 

celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(celsius, "grados Celsius son", round(fahrenheit, 2), "grados Fahrenheit")

fahrenheit = 77
celsius = (fahrenheit - 32) * 5/9
print(fahrenheit, "grados Fahrenheit son", round(celsius, 2), "grados Celsius")

# Conversión de libras a kilogramos y viceversa
# 1 libra = 0.453592 kilogramos         
pounds = 150
kilograms = pounds * 0.453592
print(pounds, "libras son", round(kilograms, 2), "kilogramos")

kilograms = 68
pounds = kilograms / 0.453592
print(kilograms, "kilogramos son", round(pounds, 2), "libras")  

#ejercicio sencillo aplicando operadores y operaciones
x =  0
x = float(x)
y = float((3 * (x**3)) - (2 * (x**2)) + (3 * x) - 1)
print("y =", y)

#La tarea es preparar un código simple para evaluar o encontrar el tiempo final de un periodo de tiempo dado, 
# expresándolo en horas y minutos. Las horas van de 0 a 23 y los minutos de 0 a 59. 
# El resultado debe ser mostrado en la consola.
#Por ejemplo, si el evento comienza a las 12:17 y dura 59 minutos, terminará a las 13:16.

hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

totalMins = mins + dura
finalHour = int((hour + (totalMins / 60)) % 24)
finalMinute = totalMins % 60
print("El evento termina a las:", finalHour, ":",finalMinute)


#if-else
income = float(input("Introduce el ingreso anual:"))

if income <= 85528:
    tax = float((income * .18) - 556.2)
    if tax <= 0: tax = float(0) 
else:
    tax = float((14839.2 + ((income - 85528)* .32)))


tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")

#if-elif-else
year = int(input("Introduce un año: "))

if year >= 1582:
    if year % 400 == 0:
        print("Año Bisiesto")
    elif year % 100 == 0:
        print("Año común")
    elif year % 4 == 0:
        print("Año Bisiesto")
    else:
        print("Año común")
else:
    print("Año no está dentro del período del calendario Gregoriano")