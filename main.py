# Main
#   Aquí se usa todo

"""
import aprendizaje._2_3_0_Wednesday
from aprendizaje._2_3_0_Wednesday import BankAccount2
from aprendizaje._2_3_0_Wednesday import BankAccount as Bank1
"""

from aprendizaje import BankAccount2

Levi = BankAccount2("Levi", 1000)
print(Levi._balance)

Levi.deposit(100)
Levi.retirar(500)