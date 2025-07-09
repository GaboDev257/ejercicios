numero = 6

#Condicional if else
if numero > 5: 
    print("El número es mayor a 5")
else:
    print("El número es menor o igual a 5") 

#Usando operadores lógicos
if numero > 5 and numero % 2 == 0:
    print("El número es mayor a 5 y es par")
else:
    print("El número no cumple ambas ondiciones")

#Bucle for
for i in range(1, 6):
    print(f"El cuadrado de {i} es {i**2}")

#Bucle while
i = 1
while i <= 5:
    if i == 4:
        break
    print(i)
    i += 1
    
x = int(input("Ingrese un número: "))
y = int(input("Ingrese otro número: "))

x = x % y
x = x % y
y = y % x

print(y)
