import sys
import random
from collections import deque
from config_params import ConfigParams
from display import display
from generate import elegir_numero, posibles_movimientos, is_42, generate_42, vecino_aleatorio, break_wall, obtener_vecinos


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

        if self.seed is not None: # si existe semilla, todos los metodos que utilices con random se quedan con un algoritmo fijo. Asi que son reproducibles.
            random.seed(self.seed)

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

    def checker(self):
        """Comprueba que no hay islas mayor de un 3x3, mirando las posiciones alrededor de los 0"""
        # maze_prueba = [['9','1','3'],['8','0','2'],['C','4','6']]
        # print(maze_prueba)
        if any(self.maze[i][j] in ('·', '*') for i in range(self.height) for j in range(self.width)):
            return False # responde false, si no esta aun bien entero para pintar

        # recorre la matriz, y se detiene en las posiciones donde hay cero '0'
        # mira los valores de sus vecinos. Si todos ellos tienen un 0 en las paredes contiguas al 0, entonces es una isla
        flag = False
        for i in range(self.height): # for i in range(height):
            for j in range(self.width): # for j in range(width):
                if self.maze[i][j] in ('0'):
                    bit_val = 0
                    for (nr, nc, bit_vec, bit_act) in obtener_vecinos(i, j):
                        if bit_act == 0 or bit_act == 2: # si el vecino esta al norte o al sur, comprueba sus posiciones este y oeste
                            contenido = self.maze[nr][nc]                                
                            num_vecino = int(contenido, 16)
                            print(f"Num_vecino = {num_vecino}")
                            bit_val += (num_vecino >> 1) & 1
                            print(f"bit_val_1 = {bit_val}")
                            bit_val += (num_vecino >> 3) & 1
                            print(f"bit_val_2 = {bit_val}")
                        if bit_act == 1 or bit_act == 3: # si el vecino esta al este o al oeste, comprueba sus posiciones norte y sur
                            contenido = self.maze[nr][nc]
                            num_vecino = int(contenido, 16)
                            print(f"Num_vecino = {num_vecino}")
                            bit_val += (num_vecino >> 0) & 1
                            print(f"bit_val_1 = {bit_val}")
                            bit_val += (num_vecino >> 2) & 1
                            print(f"bit_val_2 = {bit_val}")
                    if bit_val != 0:  
                        flag = True
        print(f"Flag = {flag}")
        return flag
        
            # if checked_all() == True: # si responde True es que se puede pintar, si responde false no se puede pintar
            #    print("Error por isla grande en pos {i}, {j}")
                # break_cero(coords) - si rompo las del cero tengo que repintar el valor de sus vecinos, o sera incompatible
                # -- es mas facil regenerar todo el laberinto entero
            
    def print_maze(self):
        printable_maze = ""
        for row_idx, row in enumerate(self.maze):
            for col_idx, cell in enumerate(row):
                print(cell, end='')
            print()  
            printable_maze += ''.join(row) + '\n'
        print()
        display(printable_maze)