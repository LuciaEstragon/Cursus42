#!/usr/bin/env python3

# ************************************************************************ #
#                                                                          #
#                                                      :::      ::::::::   #
#   ft_plant_growth.py                               ::+::    :+:    :+:   #
#                                                  +:+ +:+         +:+     #
#   By: lestrada <lestrada@student.42.es>        +#+  +:+       +#+        #
#                                              +#+#+#+#+#+   +#+           #
#   Created: 2026/04/02 09:30:00 by lestrada        #+#    #+#             #
#   Updated: 2026/04/27 09:30:00 by lestrada       ###   ########.es       #
#                                                                          #
# ************************************************************************ #

'''
¿Qué son __init__ y __str__?
Son métodos especiales (también llamados "métodos mágicos" o "dunder methods" - double underscore) que Python llama automáticamente en ciertas situaciones.

__init__ - El constructor
¿Qué significa?
"Init" = inicializar
Se llama automáticamente cuando CREAS un objeto

__str__ - Representación como string
¿Qué significa?
"Str" = string (cadena de texto)
Se llama automáticamente cuando necesitas convertir el objeto a texto
'''
class Plant:
    def __init__(self, name: str, initial_height: float, age_days: int):
        self.name = name
        self.initial_height = initial_height
        self.height = initial_height
        self.age_days = age_days
    
    def __str__(self):
        return(f"Plant: {self.name} \n" +
              f"Height: {self.height:.1f}cm \n" +
              f"Age: {self.age_days} days old \n ")

    def show(self) -> None:
        print(f"Plant: {self.name} \n" +
              f"Height: {self.height:.1f}cm \n" +
              f"Age: {self.age_days} days old \n ")

    def grow(self):
        pass
    
    def age(self):
        self.age_days += 1

class Rose(Plant):
    def grow(self) -> None:
        self.height += 0.8


class Bamboo(Plant):
    def grow(self) -> None:
        self.height += 2.5


class Cactus(Plant):
    def grow(self) -> None:
        self.height += 0.1

def simulate_growth() -> None:
    my_plant = Rose("Rose", 25.0, 30)
    print("=== Garden Plant Growth ===")
    print(my_plant)  # Aquí se usan los parámetros del constructor
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        my_plant.grow()
        my_plant.age()
        # my_plant.show()
        print(my_plant)
    total_increase = my_plant.height - my_plant.initial_height
    print(f"\nGrowth this week: {total_increase:.1f}cm")

if __name__ == "__main__":
    simulate_growth()