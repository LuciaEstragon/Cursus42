#!/usr/bin/env python3

# ************************************************************************ #
#                                                                          #
#                                                      :::      ::::::::   #
#   ft_coordinate_system.py                          ::+::    :+:    :+:   #
#                                                  +:+ +:+         +:+     #
#   By: lestrada <lestrada@student.42.es>        +#+  +:+       +#+        #
#                                              +#+#+#+#+#+   +#+           #
#   Created: 2026/05/06          by lestrada        #+#    #+#             #
#   Updated: 2026/05/10          by lestrada       ###   ########.es       #
#                                                                          #
# ************************************************************************ #

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        entrada = input("Enter coordinates (x,y,z): ").strip()
        partes = entrada.split(',')
        if len(partes) != 3:
            print("Error: need exactly 3 values separated by commas.")
            continue
        try:
            x = float(partes[0])
            y = float(partes[1])
            z = float(partes[2])
            return (x, y, z)
        except ValueError:
            print("Error: coordinates must be numbers.")


def distancia(p1: tuple[float, float, float],
              p2: tuple[float, float, float]) -> float:
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 + (p2[2]-p1[2])**2)


def main() -> None:
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates:")
    pos1 = get_player_pos()
    print(f"Player position (tuple): {pos1}")
    print(f"X: {pos1[0]}, Y: {pos1[1]}, Z: {pos1[2]}")
    dist_center = math.sqrt(pos1[0]**2 + pos1[1]**2 + pos1[2]**2)
    print(f"Distance to center (0,0,0): {dist_center:.2f}")

    print("\nSecond position:")
    pos2 = get_player_pos()
    dist_between = distancia(pos1, pos2)
    print(f"Distance between positions: {dist_between:.2f}")


if __name__ == "__main__":
    main()
