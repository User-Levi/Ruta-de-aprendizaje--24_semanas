import random
#while
#if/elif/else
#continue
#break

numero_aleatorio = random.randint(1, 100)
print(numero_aleatorio)



diesMenos = numero_aleatorio - 10
diezMas = numero_aleatorio + 10
VeinteMenos = numero_aleatorio - 20
VeinteMas = numero_aleatorio + 20
TreintaMenos = numero_aleatorio - 30
TreintaMas = numero_aleatorio + 30

intentos = 0


print("\n\
🎮 Bienvenido al juego de Adivina el Número (1-100)\n")
while intentos < 10:

    num_elegido = int(input(f"Tienes {10 - intentos} intentos: "))


    if num_elegido == numero_aleatorio:
        print(f"🎉 ¡Correcto! Adivinaste en {intentos} intentos.")
        break
    elif num_elegido >= diesMenos and num_elegido <= diezMas:
        print("Muy cerca")
        intentos += 1
    elif num_elegido >= VeinteMenos and num_elegido <= VeinteMas:
        print("Te ves acercado")
        intentos += 1
    elif num_elegido >= TreintaMas and num_elegido <= TreintaMenos:
        print("LEJOS")
        intentos += 1
    else:
        print("Ni cerca estas -_-")
        intentos += 1