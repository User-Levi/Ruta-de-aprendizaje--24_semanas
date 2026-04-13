# Manejo de Excepciones
#   try / except

import random

numero_aleatorio = random.randint(1, 100)
print(numero_aleatorio)



diesMenos = numero_aleatorio - 10
diezMas = numero_aleatorio + 10

intentos = 0


print("\n\
🎮 Bienvenido al juego de Adivina el Número (1-100)\n")
while intentos < 10:
    try:
        num_elegido = int(input(f"Tienes {10 - intentos} intentos: "))

    except ValueError:
        print("Ingresa un dato numerico")

    else: 
        if num_elegido == numero_aleatorio:

            print(f"🎉 ¡Correcto! Adivinaste en {intentos} intentos.")
            break

        elif num_elegido >= diesMenos and num_elegido <= diezMas:

            print("Muy cerca")
            intentos += 1

        else:
            print("Ni cerca estas -_-")
            intentos += 1
    finally:
        #Siempre se ejecuta, haya error o no
        pass        