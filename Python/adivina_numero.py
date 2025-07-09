import random 
 
numero_secreto = random.randint(1, 10) 
intentos = 0 
 
print("Bienvenido al juego de adivinar el número (1 al 10)") 
 
while True: 
    try: 
        intento = int(input("Ingresa tu número: ")) 
        if intento < 1 or intento > 10: 
            print("El número debe estar entre 1 y 10.") 
            continue 
        intentos += 1 
        if intento == numero_secreto: 
            print(f"¡Correcto! Adivinaste en {intentos} intentos.") 
            break 
        elif intento < numero_secreto: 
            print("Demasiado bajo. Intenta un número más alto.") 
        else: 
            print("Demasiado alto. Intenta un número más bajo.") 
    except ValueError: 
        print("Entrada inválida. Por favor ingresa un número entero.") 