"""Programa simulación cajero automático"""
class Cajero_Automatico:
    def __init__(self):
        self.total_cuenta = 0

    def total_saldo(self):
        """Devuelve el total de la cuenta"""
        return print(f"Su saldo total es: {self.total_cuenta}")

    def anadir_saldo(self):
        """Sumamos saldo al total"""
        suma_saldo = int(input("Cantidad del Ingreso: "))
        self.total_cuenta = suma_saldo + self.total_cuenta
        return print(f"Su saldo total es de: {self.total_cuenta}")

    def retirar_saldo(self):
        """Retiramos saldo de la cuenta"""
        retirar_saldo = int(input("Cantidad a Retirar: "))
        if retirar_saldo > self.total_cuenta:
            return print("La cantidad que quiere retirar no puede ser superior al total de su cuenta")
        else:
            self.total_cuenta = self.total_cuenta - retirar_saldo
            return print(f"Su saldo actual es: {self.total_cuenta}")

print("Bienvenido al Cajero Automático")
print("")
print("Por favor elija una opción: ")
print("1. Ver total cuenta")
print("2. Ingresar en cuenta")
print("3. Retirar dinero")
print("4. Salir")

cajero = Cajero_Automatico()
salir = False

while not salir:
    opcion = int(input("Opción: "))
    if opcion == 1:
        cajero.total_saldo()
    elif opcion == 2:
        cajero.anadir_saldo()
    elif opcion == 3:
        cajero.retirar_saldo()
    elif opcion == 4:
        print("Gracias por usar nuestro cajero automático")
        break

