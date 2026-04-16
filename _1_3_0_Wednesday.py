# Semana 1: Día 3: Archivo 1
#   Dict, Set, List: ejercicios

#       Alemacenar contactos con name, city and phone
#       Evitar duplicados #checkout
#       Buscar por 

Agenda = [
    {"Name": "Ana López",    "Ciudad" : "CDMX",        "Telefono" : "55-1234"},
    {"Name": "Bruno Reyes",  "Ciudad": "Guadalajara",  "Telefono" : "33-5678"},
    {"Name": "Carla Méndez", "Ciudad": "CDMX",         "Telefono" : "55-9012"},
    {"Name": "Diego Torres", "Ciudad": "Monterrey",    "Telefono" : "81-3456"},
]

print(Agenda)

def agregar_contacto():
    name_contact = str(input("Ingresa el nombre del nuevo contacto: \n"))
    city = str(input("Ingresa la ciudad del contacto nuevo: \n"))
    telefono_contact = str(input("Ingresa el número del contacto: \n"))
    localizar_agenda = str(input("Ingresa el nombre de la agenda: \n"))

    if localizar_agenda == "Agenda":
        print("Agenda localizada")

        encontrado = False

        for número in Agenda:

            if número["Telefono"] == telefono_contact:
                print("Número encontrado")
                encontrado = True
                break

        if encontrado == False:
            Agenda.append({"Name": name_contact, "Ciudad": city, "Telefono": telefono_contact})
            print("Contacto agregado")
            print(Agenda)

agregar_contacto()