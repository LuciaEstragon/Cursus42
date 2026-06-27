#!/usr/bin/env python3

# ************************************************************************ #
#                                                                          #
#                                                      :::      ::::::::   #
#   ft_plant_factory.py                              ::+::    :+:    :+:   #
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
    def __init__(self, height: float, age_days: int) -> None:
        super().__init__("Rose", height, age_days)

    def grow(self) -> None:
        self.height += 0.8


class Oak(Plant):
    def __init__(self, height: float, age_days: int) -> None:
        super().__init__("Oak", height, age_days)

    def grow(self) -> None:
        self.height += 2.5


class Cactus(Plant):
    def __init__(self, height: float, age_days: int) -> None:
        super().__init__("Cactus", height, age_days)

    def grow(self) -> None:
        self.height += 0.1


class Sunflower(Plant):
    def __init__(self, height: float, age_days: int) -> None:
        super().__init__("Sunflower", height, age_days)


class Fern(Plant):
    def __init__(self, height: float, age_days: int) -> None:
        super().__init__("Fern", height, age_days)

# --- THE PROGRAM ---


def plant_factory() -> None:
    print("=== Plant Factory Output ===")
    # creo una lista con todos mis objetos para luego con un for recorrer la lista
    garden: list[Plant] = [
        Rose(25.0, 30),
        Oak(200.0, 365),
        Cactus(5.0, 90),
        Sunflower(80.0, 45),
        Fern(15.0, 120)
    ]

    for plant in garden:
        plant.show()


if __name__ == "__main__":
    plant_factory()
