#Programa de empleados 

class Empleado:
    """1. Definir __init__ con: nombre, salario, departamento, antiguedad (años) """
    def __init__(self, name, salario, departamento, antiguedad):
        self.name = name
        self.salario = salario
        self.departamento = departamento
        self.antiguedad = antiguedad
    """ 2. Método calcular_bono(): aumenta 5% ----por cada año de antigüedad----(únicamente el aumento)"""

    def calcular_bono(self):
        salario_a_calcular = self.salario
        porcentaje = 5

        resultado = (porcentaje / 100) * salario_a_calcular
        print(resultado)  # 30
        return(resultado)

    # 3. Método dar_aumento(porcentaje)

    def dar_bono(empleado):
        salari = empleado.salario
        salari += empleado.calcular_bono()
        print(salari)

    # 4. __str__ y __repr__

    def __str__(self):
        return f"{self.name}, {self.salario}, {self.departamento}, {self.antiguedad}"
    
    def __repr__(self):
        return f"Nombre del empleado: {self.name}. Salario: {self.salario}. Departamento: {self.departamento}. Antiguedad: {self.antiguedad}"

"""
Levi = Empleado("Levi", 200, "A1", 1)
Empleado.dar_bono(Levi)
print(str(Levi))
print(repr(Levi))
"""


class Gerente(Empleado):
    def __init__(self, name: str, salario: float, equipo: list):
        # Hereda de Empleado
        super().__init__(name, salario, "Gerencia")
        #super().__init__(name) = utiliza lo que ya está arriba, no duplica la variable
        self.equipo = equipo


    # Agrega atributo: lista de empleados a cargo
    # Sobreescribe calcular_bono(): bono base del 25%
    # Agrega método: agregar_empleado(empleado)
    pass

