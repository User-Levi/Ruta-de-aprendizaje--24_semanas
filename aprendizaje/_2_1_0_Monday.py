#Class

class coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.arrancado = False
    def arrancar(self):
            self.arrancado = True
            print(f"El {self.marca} {self.modelo}, se ha arrancado")

    def detener(self):
            self.arrancado = False
            print(f"El {self.marca} {self.modelo}, se ha apagado")


tesla = coche("Tesla", "X")
chevrolet = coche("Chevrolet", "Camaro 2020")

print(type(tesla))
print(type(chevrolet))

print(f"Marca 1: {tesla.marca}. Modelo: {tesla.modelo}")
print(f"Marca 2: {chevrolet.marca}. Modelo: {chevrolet.modelo}")

tesla.arrancar()
chevrolet.arrancar()

print(tesla.arrancado)
print(chevrolet.arrancado)

tesla.detener()
chevrolet.detener()

print(tesla.arrancado)
print(chevrolet.arrancado)