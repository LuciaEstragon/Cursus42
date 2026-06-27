#!/usr/bin/env python3
import random
from collections import deque


# ---------- FUNCIONES AUXILIARES ----------
def initialize(): # NO LO USO -- QUITAR
    maze = [[None] * width for _ in range(height)]
    for i in range(height):
        for j in range(width):
            if (i, j) == start:
                maze[i][j] = '@'
            elif (i, j) == finish:
                maze[i][j] = '*'
            else:
                maze[i][j] = '·'


def obtener_vecinos(row, col):
    """Devuelve lista de tuplas (nr, nc, bit_vecino, bit_actual) para cada dirección"""
    return [
        (row-1, col, 2, 0),   # norte
        (row, col+1, 3, 1),   # este
        (row+1, col, 0, 2),   # sur
        (row, col-1, 1, 3)    # oeste
    ]

def vecino_aleatorio(row, col, maze, height, width):
    candidatos = []
    for (nr, nc, bit_vec, bit_act) in obtener_vecinos(row, col):
        if 0 <= nr < height and 0 <= nc < width:
            if maze[nr][nc] not in ('·', '@', '*') and is_42(nr, nc, (width // 2, height // 2)) == False:
                candidatos.append((nr, nc, bit_vec, bit_act))
    return random.choice(candidatos) if candidatos else None


def calcular_obligatorios(row, col, maze, height, width):
    """Construye diccionario {bit_actual: valor_requerido} según vecinos ya visitados"""
    obligatorios = {}
    for (nr, nc, bit_vec, bit_act) in obtener_vecinos(row, col):
        # Vecino fuera del mapa -> pared cerrada (1)
        if nr < 0 or nc < 0 or nr >= height or nc >= width:
            obligatorios[bit_act] = 1
        else:
            contenido = maze[nr][nc]
            # Solo nos interesan vecinos que ya tengan un número asignado (hex)
            if contenido not in ('·', '@', '*'):
                num_vecino = int(contenido, 16)
                bit_val = (num_vecino >> bit_vec) & 1
                obligatorios[bit_act] = bit_val
    return obligatorios

def cumple(num, obligatorios):
    """Verifica si num cumple todas las restricciones del diccionario"""
    for pos, valor in obligatorios.items():
        if ((num >> pos) & 1) != valor:
            return False
    return True

def elegir_numero(row, col, maze, height, width):
    """Elige un número aleatorio (0..14) que cumpla las restricciones de los vecinos"""
    obligatorios = calcular_obligatorios(row, col, maze, height, width)
    candidatos = [n for n in range(16) if n != 15 and cumple(n, obligatorios)]
    # if not candidatos: # por aqui no pasa nunca
        # Si no hay candidatos (caso raro), devolvemos 0 (todas las paredes abiertas)
    #    return 0
    return random.choice(candidatos)

def elegir_numero_sin_bucles(row, col, maze, height, width, visitados=None):
    """
    Elige un número aleatorio (0..14) que cumpla las restricciones de los vecinos
    y evite crear conexiones a celdas ya visitadas (excepto el padre)
    """
    obligatorios = calcular_obligatorios(row, col, maze, height, width)
    
    # Si tenemos visitados, forzamos paredes cerradas hacia ellos
    if visitados is not None and (row, col) not in visitados:
        for (nr, nc, bit_vec, bit_act) in obtener_vecinos(row, col):
            if 0 <= nr < height and 0 <= nc < width:
                if (nr, nc) in visitados and (nr, nc) != (row, col):
                    # Forzar que este bit sea 1 (pared cerrada)
                    obligatorios[bit_act] = 1
    
    candidatos = [n for n in range(16) if n != 15 and cumple(n, obligatorios)]
    return random.choice(candidatos) if candidatos else 0

def cerrar_muro(row, col, maze, bit):
    """Cierra un muro en la celda actual cambiando el bit a 1"""
    numero_actual = int(maze[row][col], 16)
    # Poner el bit a 1
    numero_actual |= (1 << bit)
    maze[row][col] = format(numero_actual, 'X')

def cerrar_muro_vecino(row, col, maze, bit):
    """Cierra un muro en la celda vecina cambiando el bit a 1"""
    if maze[row][col] not in ('·', '@', '*'):
        numero_actual = int(maze[row][col], 16)
        # Poner el bit a 1
        numero_actual |= (1 << bit)
        maze[row][col] = format(numero_actual, 'X')

def posibles_movimientos(row, col, maze, height, width, visitados=None):
    """Devuelve lista de vecinos a los que podemos movernos según el número de la celda actual"""
    movimientos = []
    numero_actual = int(maze[row][col], 16)  # asumimos que la celda ya tiene número
    for (nr, nc, bit_vec, bit_act) in obtener_vecinos(row, col):
        # Verificar si el bit correspondiente está abierto (0)
        if ((numero_actual >> bit_act) & 1) == 0:
            # Asegurarse que el vecino está dentro del mapa
            if (0 <= nr < height and 0 <= nc < width):
                ## evita bucles
                if visitados is not None and (nr, nc) in visitados: #if maze[nr][nc] not in ('·', '*'):
                    # CERRAR EL MURO en la celda actual
                    cerrar_muro(row, col, maze, bit_act)
                    # CERRAR EL MURO en la celda vecina
                    cerrar_muro_vecino(nr, nc, maze, bit_vec)
                else:
                    movimientos.append((nr, nc))
    return movimientos

def break_wall(maze, height, width):
    """Busca una celda vacía ('·' o '*') y desde ella rompe la pared de un vecino con número."""
    for i in range(height):
        for j in range(width):
            if maze[i][j] in ('·', '*'):
                chose_vec = vecino_aleatorio(i, j, maze, height, width)
                if chose_vec is not None:
                    a, b = pos_break(maze, chose_vec)   # modifica el vecino
                    return (a, b)   # devuelve la celda que ahora tiene el camino abierto
    return None   # si no hay ninguna celda con vecino válido (caso raro)
    
def pos_break(maze, chose_vec):
    (nr, nc, bit_vec, bit_act) = chose_vec
    # Leer el contenido actual de la celda vecina
    contenido = maze[nr][nc]
    num_vecino = int(contenido, 16)   # valor numérico (0-15)
    # Poner el bit en la posición bit_vec a 0 (los demás bits se mantienen igual)
    num_vecino &= ~(1 << bit_vec)     # usar máscara de bits
    # Convertir de vuelta a hexadecimal (sin '0x', mayúscula)
    maze[nr][nc] = format(num_vecino, 'X')
    return (nr, nc)

def is_42(row, col, middle):
    return (row, col) in get_42_coords(middle)

def get_42_coords(middle):
    mc, mr = middle  # (col_centro, fila_centro)
    return [
        (mr - 2, mc - 3), (mr - 1, mc - 3), (mr, mc - 3),
        (mr, mc - 2), (mr, mc - 1),
        (mr + 1, mc - 1), (mr + 2, mc - 1),
        (mr - 2, mc + 1), (mr - 2, mc + 2), (mr - 2, mc + 3),
        (mr - 1, mc + 3), (mr, mc + 3),
        (mr, mc + 2), (mr, mc + 1),
        (mr + 1, mc + 1), (mr + 2, mc + 1),
        (mr + 2, mc + 2), (mr + 2, mc + 3)
    ]

def generate_42(maze, middle):
    for (row, col) in get_42_coords(middle):
        if 0 <= row < len(maze) and 0 <= col < len(maze[0]):
            maze[row][col] = 'F'

