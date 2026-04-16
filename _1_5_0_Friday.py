#Funciones y sus parametros

def saludo(name, age):
    print(f"¡Hola {name}! tienes {age} años")

saludo("Levi", 17)

def salu2(name, idioma="Español"): # Hice el idioma predeterminado el "Español"
    print(f"¡Hola {name}! Idioma: {idioma}")

salu2("Levy")
salu2("Mateo", "Frances")

print("-----------------\n\
-----------------")

#-----------------------------------------

# *args
'''
Se utiliza cuando no se sabe cuantos elementos se colocaran
Estos se empacan en una tupla
'''

def sumas(*args):
    total = 0
    for i in args:
        total += i
    return total

print(sumas(1, 2, 3))        # 6
print(sumas(10, 20, 30, 40)) # 100


# **kwargs

def diccionarios(**kwargs):
    for i, v in kwargs.items():
        print(f"{i}: {v}")

diccionarios(name="Levis", ciudad="CMDX")

print("-----------------\n\
-----------------")