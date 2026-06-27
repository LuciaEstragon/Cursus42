import sys
import random
from collections import deque
from config_params import ConfigParams
from display import display
from generate import elegir_numero, posibles_movimientos, is_42, generate_42, vecino_aleatorio, break_wall


class Maze(ConfigParams):
    def __init__(self, filename):
        super().__init__(filename) # Llama al constructor de ConfigParams
        self.maze = None   # se creará en generate_maze

    def get_output_file(self):
        try:
            with open(self.out_file, 'w') as f_out:
                write_lines = [''.join(row) + '\n' for row in self.maze]
                f_out.writelines(write_lines)
        except PermissionError as e:
            print(f"[STDERR] Error opening file '{self.out_file}': {e}", file=sys.stderr)
            print("Data not saved.")
        except Exception as e:
            print(f"[STDERR] Unexpected error: {e}", file=sys.stderr)

    def generate_maze(self):
        # ---------- BUCLE PRINCIPAL: RECORRIDO BFS ----------
        # Inicializar la matriz
        self.maze = [['·' for _ in range(self.width)] for _ in range(self.height)]
        self.maze[self.start[0]][self.start[1]] = '@'  # esto no lo estoy usando mucho para nada
        self.maze[self.finish[0]][self.finish[1]] = '*' # esto no lo estoy usando mucho para nada

        # Genero el 42
        if self.width > 9 and self.height > 7:
            generate_42(self.maze, (self.width // 2, self.height // 2))

        # Usamos una cola con las posiciones pendientes de procesar
        cola = deque()
        cola.append(self.start)

        # Ahora bucle principal: mientras haya celdas pendientes
        while cola:
            row, col = cola.popleft()
            
            # Si ya no es '·' (podría haber sido asignada por otro camino) la saltamos
            # esto da problemas para intentar romper el laberinto cuando no se ha rellenado todo
            # if maze[row][col] != '·' and maze[row][col] != '@' and maze[row][col] != '*':
            #    continue
            if is_42(row, col, (self.width // 2, self.height // 2)):
                continue

            # 1. Calcular número para esta celda según sus vecinos
            num_celda = elegir_numero(row, col, self.maze, self.height, self.width)
            self.maze[row][col] = format(num_celda, 'X')
            
            # 2. Determinar hacia qué vecinos podemos movernos (bits abiertos)
            for nr, nc in posibles_movimientos(row, col, self.maze, self.height, self.width):
                if (self.maze[nr][nc] == '·' or self.maze[nr][nc] == '*') and (nr, nc) not in cola:
                    cola.append((nr, nc))
            
            # 3. Para quedarme dentro del bucle si aun no he dado valor a todas las casillas
            if not cola and any(self.maze[i][j] in ('·', '*') for i in range(self.height) for j in range(self.width)):
                coords = break_wall(self.maze, self.height, self.width)   # <-- sin row, col
                if coords:
                    cola.append(coords)

    def print_maze(self):
        printable_maze = ""
        for row_idx, row in enumerate(self.maze):
            for col_idx, cell in enumerate(row):
                print(cell, end='')
            print()  
            printable_maze += ''.join(row) + '\n'
        print()
        display(printable_maze)