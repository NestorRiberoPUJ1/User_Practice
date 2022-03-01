import imp
from User import User

Jhon= User("Jhon")
Mary= User("Mary")
Luke= User("Luke")

Jhon.hacerDeposito(1000).hacerDeposito(500).hacerDeposito(250).hacerRetiro(550).mostrarBalance()

Mary.hacerDeposito(1000).hacerDeposito(500).hacerRetiro(150).hacerRetiro(250).mostrarBalance()

Luke.hacerDeposito(10000).hacerRetiro(550).hacerRetiro(100).hacerRetiro(350).mostrarBalance()

Jhon.transfer_Cash(Luke,200).mostrarBalance()
Luke.mostrarBalance()