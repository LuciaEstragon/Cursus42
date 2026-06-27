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

class Plant:
    def __init__(self, my_name: str, my_height: float, my_age: int) -> None:
        self.name = my_name
        self.height = my_height
        self.age_days = my_age
        self.initial_height = my_height

    def show(self) -> None:
        print(f"Plant: {self.name} \n" +
              f"Height: {self.height}cm \n" +
              f"Age: {self.age_days} days old \n ")

    def age(self) -> None:
        self.age_days += 1

    def grow(self) -> None:
        pass


class Rose(Plant):
    def grow(self) -> None:
        self.height += 0.8


class Bamboo(Plant):
    def grow(self) -> None:
        self.height += 2.5


class Cactus(Plant):
    def grow(self) -> None:
        self.height += 0.1

# --- THE PROGRAM ---


def simulate_growth() -> None:
    my_plant = Rose("Rose", 25.0, 30)
    print("=== Garden Plant Growth ===")
    print(my_plant)
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        my_plant.grow()
        my_plant.age()
        print(my_plant)
    total_increase = my_plant.height - my_plant.initial_height
    print(f"\nGrowth this week: {total_increase:.1f}cm")


if __name__ == "__main__":
    simulate_growth()
