import imp
from User import User

Jhon= User("Jhon")
Mary= User("Mary")
Luke= User("Luke")

Jhon.hacerDeposito(1000)
Jhon.hacerDeposito(500)
Jhon.hacerDeposito(250)
Jhon.hacerRetiro(550)
Jhon.mostrarBalance()

Mary.hacerDeposito(1000)
Mary.hacerDeposito(500)
Mary.hacerRetiro(150)
Mary.hacerRetiro(250)
Mary.mostrarBalance()

Luke.hacerDeposito(10000)
Luke.hacerRetiro(550)
Luke.hacerRetiro(100)
Luke.hacerRetiro(350)
Luke.mostrarBalance()

Jhon.transfer_Cash(Luke,200)
Jhon.mostrarBalance()
Luke.mostrarBalance()