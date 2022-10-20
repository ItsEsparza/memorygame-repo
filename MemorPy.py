import random
import time

# Bienvenida (Bienvenida, regla e introducción de usernames)
print("-----Bienvenido a memopy-----\n")
reglas = input("¿Conoces las reglas?(Si/No): ")
reglas = reglas.upper()
if reglas == "SI":
    pass
else:
    print("\n\n\n\n\n"
        "                           --------Reglas--------\n"
          "1. Cada jugador tiene 5 vidas, cada intento fallido restara 1 vida de su contador\n"
          "2. Al quedarse un jugador sin vidas la tabla sera recreada y sera el turno del siguiente jugador\n"
          "3. El ganador se medira en un sistema de puntos que se explicara mas adelante\n"
          "4. Si un jugador logra descubrir la tabla completa automaticante ganara el juego\n"
          "5. Si un jugador logra descubrir 3 numeros iguales seguidos obtendra una vida extra\n"
          "6. Los valores deberan ser introducidos bajo el siguiente formato: (fila)(columna) | Ejemplo: A1\n"
          "7. El limite de jugadores es 5\n"
          "8. Al equivocarte tendras 3 segundos para visualizar el lugar de los valores erroneos, traes este tiempo los"
          "valores volveran a dejar de ser visibles\n"
          "9. Introduce exit en cualquier turno para terminar la partida"
          )
    input("\n\n\n\nEscribe ok cuando hayas leido las reglas: ")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
        "                           --------Sistema de puntuación--------\n"
          "Cada par de numeos iguales descubiertos por un jugador le otorgara un punto extra\n"
          "Los puntos seran sumados al final de la partida y se mostrara la tabla de puntuaciones")
    input("\n\n\n\n\n\n\n\nEscribe ok cuando hayas entendido el sistema de puntuación: ")

# Lista de jugadores
jugadores = []
# Introducir jugadores
while True:
    NDJ = input("¿Cuantos jugadores jugaran esta partida?: ")
    if NDJ in ["1", "2", "3", "4", "5"]:
        NDJ = int(NDJ)
    else:
        print("Solo se aceptan valores numericos entre 1 y 5")
        continue

    if NDJ in [1, 2, 3, 4, 5]:
        break
    else:
        print("El numero de jugadores introducidos no es valido")
        continue

for i in range(NDJ):
    jugador = input(f"Jugador {i+1} escribe tu nombre: ")
    jugadores += [jugador[0:3]]

# Puntaje y vidas
puntos = []
vidas = []
for i in range(NDJ):
    puntuación = 0
    puntos += [puntuación]

for i in range(NDJ):
    vidas_iniciales = 5
    vidas += [vidas_iniciales]

# Tabla de puntuaciones
def print_tablapuntos():
    tabla_puntos = [["+------------------+"],
                    ["| Jugador |"," Puntos |"],
                    ["+---------+--------+"],]
    for i in tabla_puntos:
        print()
        for j in i:
            print(j, end="")
    print("")
    for c,d in zip(jugadores,puntos):
        print("|{:>6}   |   {:<5}|".format(c,d))
    print("+---------+--------+")

# Tabla sin resolver
board = [["   ", 1, 2, 3, 4, 5, 6],
         ["  +-------------+"],
         ["A |", "-", "-", "-", "-", "-", "-", "|"],
         ["B |", "-", "-", "-", "-", "-", "-", "|"],
         ["C |", "-", "-", "-", "-", "-", "-", "|"],
         ["D |", "-", "-", "-", "-", "-", "-", "|"],
         ["E |", "-", "-", "-", "-", "-", "-", "|"],
         ["F |", "-", "-", "-", "-", "-", "-", "|"],
         ["  +-------------+"]]


def print_board():
    for i in board:
        print()
        for j in i:
            print(j, end=" ")

# Tabla resuelta
header = ["   ", 1, 2, 3, 4, 5, 6]
divider = ["  +-------------+"]
t1 = ["A |", ]
t2 = ["B |", ]
t3 = ["C |", ]
t4 = ["D |", ]
t5 = ["E |", ]
t6 = ["F |", ]
bottom = " ", "+-------------+"

# Asignación de numeros
def create_table(t):
    for i in range(0, 6):
        item = random.randrange(1, 9)
        t += [item]


create_table(t1)
create_table(t2)
create_table(t3)
create_table(t4)
create_table(t5)
create_table(t6)

solved_board = header, divider, t1, t2, t3, t4, t5, t6, bottom

def print_solvedboard():
    for i in solved_board:
        print()
        for j in i:
            print(j, end=" ")

# Sistema de introducción de datos por parte del usuario
def datos():
    global columna
    global fila
    global vidas
    while True:
        valor_a_reemplazar = input("Introduce los valores que quieras revelar: ")
        valor_a_reemplazar = valor_a_reemplazar.upper()
        if valor_a_reemplazar == "EXIT":
            exit()
        if len(valor_a_reemplazar) != 2:
            print("El valor introducido es incorrecto")
            continue
        columna = (valor_a_reemplazar[1])
        fila = valor_a_reemplazar[0]
        fila.upper()
        if columna in ["1", "2", "3", "4", "5", "6"]:
            columna = int(columna)
            pass
        else:
            print("columna tiene que ser un valor numerico")
            continue
        if fila in ["A", "B", "C", "D", "E", "F"] and columna in [1, 2, 3, 4, 5, 6]:
            break
        else:
            print("Los valores introducidos son invalidos")
            continue
    if fila == "A":
        fila = int(2)
    elif fila == "B":
        fila = int(3)
    elif fila == "C":
        fila = int(4)
    elif fila == "D":
        fila = int(5)
    elif fila == "E":
        fila = int(6)
    elif fila == "F":
        fila = int(7)

    return fila
    return columna

def datos1():
    global columna1
    global fila1
    global fila
    global columna
    while True:
        while True:
            valor_a_reemplazar = input("Introduce los valores que quieras revelar: ")
            valor_a_reemplazar = valor_a_reemplazar.upper()
            if valor_a_reemplazar == "EXIT":
                exit()
            if len(valor_a_reemplazar) != 2:
                print("El valor introducido es incorrecto")
                continue
            columna1 = (valor_a_reemplazar[1])
            fila1 = valor_a_reemplazar[0]
            fila1[0].upper()
            if columna1 in ["1", "2", "3", "4", "5", "6"]:
                columna1 = int(columna1)
                pass
            else:
                print("El valor de columna no es valido")
                continue
            if fila1 in ["A", "B", "C", "D", "E", "F"] and columna1 in [1, 2, 3, 4, 5, 6]:
                break
            else:
                print("Los valores introducidos son invalidos")
                continue
        if valor_a_reemplazar == "EXIT":
            exit()
        if fila1 == "A":
            fila1 = int(2)
        elif fila1 == "B":
            fila1 = int(3)
        elif fila1 == "C":
            fila1 = int(4)
        elif fila1 == "D":
            fila1 = int(5)
        elif fila1 == "E":
            fila1 = int(6)
        elif fila1 == "F":
            fila1 = int(7)

        if fila != fila1 or columna != columna1:
            break
        else:
            print("Ese valor ya fue revelados, introduce otro valor")
            continue

    return fila1
    return columna1

# Sistema de reemplazo de datos en las tablas
def reemplazo():
    board[fila][columna] = solved_board[fila][columna]
    print_board()

def reemplazo1():
    board[fila1][columna1] = solved_board[fila1][columna1]
    print_board()

# Turno de un usuario
turno = 0
def tiro():
    global vidas
    global puntos
    global turno
    global jugadores
    global valor_a_reemplazar
    print_board()
    while turno < NDJ:
        print(f"\nTurno: {jugadores[turno]}")
        print(f"Vidas: {vidas[turno]}")
        datos()
        reemplazo()
        print("\n")
        datos1()
        reemplazo1()



        # Si los valores indicados coinciden
        if board[fila1][columna1] == board[fila][columna]:
            puntos[turno] = puntos[turno]+1
            print(f"\nRevelaste un numero y ganas 1 punto | Puntos Actuales: ", puntos[turno])
            print_board()
            pass
        # Si los valores indicados no coinciden
        else:
            vidas[turno] = vidas[turno]-1
            print(f"\nLas cartas que seleccionaste no coinciden, perdiste una vida | Vidas Restantes: ", vidas[turno])
            time.sleep(3)
            print(f"\n"*100)
            # Verificar si hay jugadores y avanzar al siguiente
            if vidas[turno] == 0:
                turno += 1
                if turno == NDJ:
                    break
                else:
                    print(f"\nTe quedaste sin vidas, es el turno de {jugadores[turno]}")
            board[fila1][columna1] = "-"
            board[fila][columna] = "-"
            print_board()

tiro()
print("\n\n Fin de la partida. Gracias por jugar :)\n\nEste es el tablero resuelto:")
print_solvedboard()
print_tablapuntos()