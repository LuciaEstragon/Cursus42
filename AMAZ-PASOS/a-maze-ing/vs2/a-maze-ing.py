#!/usr/bin/env python3

import sys
# from config_params import ConfigParams   # Tu clase ConfigParams (archivo config_params.py)
from maze import Maze                    # Tu clase Maze (archivo maze.py)

# Check that only one configuration file is given
def main():
    num_args = len(sys.argv) - 1
    if num_args != 1 :
        if num_args < 1 :
            print("ERROR: A configuration file needs to be provided.")
        else:
            print("ERROR: Too many arguments have been given.")
        print("Please, call the script as follows: \"python3", sys.argv[0], "filename\"")
        exit()

    maze = Maze(sys.argv[1])
    if not maze.parse():
        print("ERROR: failure parsing configuration file")
        exit()

    print("Configuration file was parsed successfully")

    print()
    checked = False
    while (checked == False):
        maze.generate_maze()
        checked = maze.checker()
    maze.resolve()
    maze.print_maze()
    coord_caminos = maze.resolve()
    direcciones = maze.convert_path_to_directions(coord_caminos)
    print(direcciones)
    maze.get_output_file()
        

if __name__ == "__main__":
    main()
    