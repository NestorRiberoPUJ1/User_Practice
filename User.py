class User:

    def __init__(self, nombre):
        self.nombre = nombre
        self.cash = 0

    def hacerRetiro(self, cantidad):
        self.cash -= cantidad
        return self

    def hacerDeposito(self, cantidad):
        self.cash += cantidad
        return self

    def mostrarBalance(self):
        print(f"{self.nombre}, Balance: ${self.cash}")
        return self

    def transfer_Cash(self,receiper,amount):
        self.cash -=amount
        receiper.cash += amount
        return self