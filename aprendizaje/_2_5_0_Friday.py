'''
Friday:
    Manejo de archivos,
    Pathlib,
    Entornos Virtuales,
    pip

'''
import csv
import json

#open(ruta, modo, encoding)

with open("/home/levi/Documentos/ingenieria/python/aprendizaje/text.txt", "r", encoding="utf-8") as f:
# r leer
# w escribir
# a agregar al final
# x crear
# .. subir de nivel
# as: asignar alias (apodo)
    contenido = f.read()
    print(contenido)

#Escribir en CSV
estudiantes = [
    ["Nombre", "Edad", "Promedio"]
    ["Aña", 22, 9.5]
    ["Mateo", 18, 8.4]
    ["David", 21, 7,5]
]

'''
        with open("estudiantes.csv", "w", newline="", encoding="utf-8") as f:
            escritor = csv.writer(f)
            escritor.writerows(estudiantes)

        # LEER CSV como listas
        with open("estudiantes.csv", "r", encoding="utf-8") as f:
            lector = csv.reader(f)
            for fila in lector:
                print(fila)

        # LEER CSV como diccionarios (¡MUY útil!)
        with open("estudiantes.csv", "r", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                
                print(f"{fila['Nombre']} tiene promedio {fila['Promedio']}")
'''

#-----------------------------------------------------------------------


#Escribir en JSON
datos = {
    "nombre": "Ana López",
    "edad": 22,
    "materias": ["POO", "Algoritmos", "Redes"],
    "activo": True,
    "promedio": 9.2,
}


'''
        # ESCRIBIR JSON
        with open("alumno.json", "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
            # indent=4 → formato legible
            # ensure_ascii=False → permite acentos y ñ

        # LEER JSON
        with open("alumno.json", "r", encoding="utf-8") as f:
            alumno = json.load(f)
            print(alumno["nombre"])         # Ana López
            print(alumno["materias"][0])    # POO

        # Convertir dict → string JSON (para APIs)
        texto_json = json.dumps(datos, indent=2)

        # Convertir string JSON → dict
        datos2 = json.loads(texto_json)
'''

#-------------------------------------------------------------------