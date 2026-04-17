class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self._balance = balance
        self.__pin = "1234"


    @property
    def balance(self):
        """Getter: se llama cuando haces cuenta.balance"""
        return self._balance
    
    @balance.setter
    def balance(self, amount: float):
        """Setter: se llama cuando haces cuenta.balance = x"""
        if amount <= 0:
            raise ValueError("El saldo no puede ser negativo")
        self._balance = amount


    def __repr__(self):
        return f"Nombre de cuenta: {self.owner}. Balance: {self._balance}. Pin: {self.__pin}"


"""
cuenta = BankAccount("Ana", 1500)
print(cuenta)

print(cuenta._balance)       # funciona, pero es mala práctica
#print(cuenta.__pin)          # AttributeError ← Python lo renombró
print(cuenta._BankAccount__pin)  # así se accede, pero NUNCA hagan esto


cuenta._balance = 10     #-10 manda error en VSC (se cumple lo esperado)
"""

separación_de_bloques = "-----------------------------"
#-------------------------------------------------------------------------

class BankAccount2:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self._balance = balance
        self._transactions = []  # historial

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("El depósito debe ser mayor a cero")
        self._balance += amount
        self._transactions.append(f"+ ${amount:.2f}")
        print(f"Depósito exitoso. Nuevo saldo: ${self._balance:.2f}")

    def retirar(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("El retiro debe ser mayor a cero")
        if amount > self._balance:
            raise ValueError("Saldo insuficiente")
        self._balance -= amount
        self._transactions.append(f"- ${amount:.2f}")
        print(f"Retiro exitoso. Nuevo saldo: ${self._balance:.2f}")

    @property
    def statement(self):
        """Genera un estado de cuenta"""
        lines = [f"=== Cuenta de {self.owner} ==="]
        lines += self._transactions if self._transactions else ["Sin movimientos"]
        lines.append(f"Saldo actual: ${self._balance:.2f}")
        return "\n".join(lines)

    @staticmethod
    def validate_amount(amount: float) -> bool:
        """Valida que un monto sea positivo y tenga máximo 2 decimales"""
        if amount <= 0:
            return False
        # Verificar que no tenga más de 2 decimales
        return round(amount, 2) == amount
    

"""
Levi = BankAccount2("Levi", 1000)
Levi.deposit(100)
"""

#@classmethod

class Persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def desde_texto(cls, texto):
        name, age = texto.split(",")
        return cls(name, int(age))
    
"""
p = Persona.desde_texto("Levis, 17")
print(p.name)
print(p.age)
"""