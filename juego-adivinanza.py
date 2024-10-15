

import random


numero_secreto = random.randint(1,100)
adivinado = False
print("Bienvenido al juego de adivinar")

while not adivinado:
    entrada = input("Introduce un numero del 1 al 99: ")
    numero = int(entrada)

    if numero == numero_secreto:
        print("felicitaciones")
        adivinado = True 
    elif numero > numero_secreto:
        print("el numero es menor")
    else:
        print("el numero es mayor")
    
