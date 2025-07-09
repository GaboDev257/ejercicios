num = int(input("Ingresa un número: "))

if num > 1: 
    for i in range(2, int(num ** 0.5) + 1): 
        if num % i == 0: 
            print("No es primo") 
            break 
    else: 
        print("Es primo") 
else: 
    print("No es primo") 