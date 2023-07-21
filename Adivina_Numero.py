import random

print("Adivina el número que estoy pensando del 1 al 100")
numero_aleatorio = random.randint(1, 100)
intentos = []
contador_intentos = 0

while True:
    numero = int(input("\nPonga el número que estoy pensando: "))

    if numero == numero_aleatorio:
        print("Has acertado!!!")
        print(f"Has hecho {contador_intentos} intentos")
        print(f"Los números que has puesto son: {intentos}")
        break

    else:
        pista = input("Lo siento, ese no es el número que estoy pensando, quieres una pista (s/n): ")
        contador_intentos += 1
        intentos.append(numero)

        if pista == 's':
            if numero < numero_aleatorio:
                print("El número que has puesto es menor al que yo estoy pensando")
            else:
                print("El número que has puesto es mayor al que yo estoy pensando")
        elif pista == 'n':
            print("Mucho ánimo, seguro que la próxima lo consigues")

