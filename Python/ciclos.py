#============CICLO WHILE==============
# Este programa solicita números al usuario y determina cuál es el más grande.

# Almacena el actual número más grande aquí.
largest_number = -999999999

# Ingresa el primer valor.
number = int(input("Introduce un número o escribe -1 para detener: "))

# Si el número no es igual a -1, continuaremos
while number != -1:
    # ¿Es el número más grande que el valor de largest_number?
    if number > largest_number:
        # Sí si, se actualiza largest_number.
        largest_number = number
    # Ingresa el siguiente número.
    number = int(input("Introduce un número o escribe -1 para detener: "))

# Imprime el número más grande
print("El número más grande es:", largest_number)


# Este programa lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares.
# El programa termina cuando se ingresa un cero.

odd_numbers = 0
even_numbers = 0

# Lee el primer número.
number = int(input("Introduce un número o escribe 0 para detener: "))

# 0 termina la ejecución.
while number != 0:
    # Verificar si el número es impar.
    if number % 2 == 1:
        # Incrementar el contador de números impares odd_numbers.
        odd_numbers += 1
    else:
        # Incrementar el contador de números pares even_numbers.
        even_numbers += 1
    # Leer el siguiente número.
    number = int(input("Introduce un número o escribe 0 para detener: "))

# Imprimir resultados.
print("Cuenta de números impares:", odd_numbers)
print("Cuenta de números pares:", even_numbers)


# Este programa simula un bucle infinito hasta que el usuario ingresa el número secreto.
secret_number = 777

number = int(input("Ingresa un número: "))

while number != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    number = int(input("Ingresa un número: "))
print("¡Bien hecho, muggle! Eres libre ahora")


#============CICLO FOR=============
# Este programa imprime las potencias de 2 desde 0 hasta 15.
power = 1
for expo in range(16):
    print("2 a la potencia de", expo, "es", power)
    power *= 2
    

# break - ejemplo

print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")


# continue - ejemplo

for numero in range(1, 6):  # Esto generará números del 1 al 5
    if numero == 3:
        continue  # Si el número es 3, salta el resto de esta iteración y ve a la siguiente
    print(numero)
    

#break ejemplo con while
while True:
    word = input("Ingresa una palabra: ")
    if word == "chupacabra":
        break
print("¡Has dejado el bucle con éxito!")

#ejemplo de continue con for
# Este programa solicita al usuario que ingrese una palabra y luego imprime las letras de la palabra
user_word = input("Ingrese una palabra: ")# Indicar al usuario que ingrese una palabra
user_word = user_word.upper()# y asignarlo a la variable user_word.

for letter in user_word:
    if letter == "A": 
        continue
    elif letter == "E": 
        continue
    elif letter == "I": 
        continue
    elif letter == "O": 
        continue
    elif letter == "U": 
        continue
    else:
        print(letter)

#imprimir la palabra sin vocales concatenada
word_without_vowels = ""

user_word = input("Ingrese una palabra: ")# Indicar al usuario que ingrese una palabra
user_word = user_word.upper()# y asignarlo a la variable user_word.

for letter in user_word:
    if letter == "A": 
        continue
    elif letter == "E": 
        continue
    elif letter == "I": 
        continue
    elif letter == "O": 
        continue
    elif letter == "U": 
        continue
    else:
        word_without_vowels += letter
print(word_without_vowels) #imprimir la palabra sin vocales
    

# Este programa calcula la altura de una pirámide con bloques.
# La altura de la pirámide se incrementa en 1 bloque por cada capa. 
blocks = int(input("Ingresa el número de bloques: "))

height = 0     # Inicializamos la altura de la pirámide
blocks_needed_for_current_layer = 1 # Los bloques necesarios para la primera capa

while blocks >= blocks_needed_for_current_layer:
    # Si tenemos suficientes bloques para la capa actual
    blocks -= blocks_needed_for_current_layer  # Usamos los bloques para la capa actual
    height += 1                                # Incrementamos la altura de la pirámide
    blocks_needed_for_current_layer += 1       # La siguiente capa necesitará un bloque más

print("La altura de la pirámide es:", height)


# Este programa implementa la Conjetura de Collatz.
# La Conjetura de Collatz establece que cualquier número natural positivo eventualmente llegará a 1
# Pedimos al usuario que ingrese un número natural (entero no negativo y no cero)
number = int(input("Ingresa un número natural (entero positivo): "))

# Validamos que el número sea positivo
if number <= 0:
    print("El número debe ser un entero positivo y no cero.")
else:
    c0 = number  # Asignamos el número inicial a c0
    pasos = 0    # Inicializamos el contador de pasos

    print("Secuencia de Collatz:")
    print(int(c0)) # Imprimimos el valor inicial

    # El bucle continúa mientras c0 sea diferente de 1
    while c0 != 1:
        if c0 % 2 == 0:  # Si c0 es par
            c0 = c0 / 2  # c0 se convierte en c0 / 2
        else:            # Si c0 es impar
            c0 = 3 * c0 + 1 # c0 se convierte en 3 * c0 + 1
        
        # Imprimimos el valor actual de c0 (convertido a entero para eliminar decimales .0)
        print(int(c0))
        
        pasos += 1 # Incrementamos el contador de pasos

    print("\nSe necesitaron", pasos, "pasos para llegar a 1.")
    
#Ejercicio
#Crea un bucle for que cuente de 0 a 10, e imprima números impares en la pantalla.
for i in range(11):
    if i % 2 != 0:
        print(i)

#Crea un bucle while que cuente de 0 a 10, e imprima números impares en la pantalla.
x = 1

while x < 10:
    if x % 2 != 0:
        print(x)
    x += 1
    
#Crea un programa con un bucle for y una sentencia break. 
# El programa debe iterar sobre los caracteres en una dirección de correo electrónico, 
# salir del bucle cuando llegue al símbolo @ e imprimir la parte antes de @ en una línea

email = "estoesunmail@test.io"

for char in email:
    if char == '@':
        break
    print(char, end='')  # Imprime el carácter sin salto de línea
    

#Crea un programa con un bucle for y una sentencia continue. 
# El programa debe iterar sobre una cadena de dígitos, 
# reemplazar cada 0 con x, e imprimir la cadena modificada en la pantalla.

for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")

