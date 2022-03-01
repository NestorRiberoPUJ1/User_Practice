class User:

    def __init__(self, nombre):
        self.nombre = nombre
        self.cash = 0

    def hacerRetiro(self, cantidad):
        self.cash -= cantidad

    def hacerDeposito(self, cantidad):
        self.cash += cantidad

    def mostrarBalance(self):
        print(f"{self.nombre}, Balance: ${self.cash}")

    def transfer_Cash(self,receiper,amount):
        self.cash -=amount
        receiper.cash += amount