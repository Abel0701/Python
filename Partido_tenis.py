class PartidoTenis:
    def __init__ (self):
        self.player1 = 0
        self.player2 = 0

    def obtener_puntuacion(self, player):
        if player == 1:
            self.player1 += 1
        elif player == 2:
            self.player2 += 1

    def partido_tenis(self):
        puntuacion = ""
        puntos = ["Love", 15, 30, 40, "Deuce"]

        if self.player1 < 4 and self.player2 < 4:
            puntuacion = f"{puntos[self.player1]} - {puntos[self.player2]}"

        elif self.player1 == self.player2:
            puntuacion = "Deuce"

        elif abs(self.player1 - self.player2) == 1:
            lider = 1 if self.player1 > self.player2 else 2
            puntuacion = f"Ventaja {lider}"
        else:
            lider = 1 if self.player1 > self.player2 else 2
            puntuacion = f"Gana {lider}"

        return puntuacion


# Prueba
puntuacion = PartidoTenis()

print("Puntuación inicial: ", puntuacion.partido_tenis())

salir = True

while salir:
    punto = input("Que jugador ha ganado el punto (P1/P2), para salir marque P3: ")
    if punto == "P1":
        puntuacion.obtener_puntuacion(1)
    elif punto == "P2":
        puntuacion.obtener_puntuacion(2)

    print("Puntuación actual: ",puntuacion.partido_tenis())

    if punto == "P3":
        salir = False




