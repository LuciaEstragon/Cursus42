#!/usr/bin/env python3

# ************************************************************************ #
#                                                                          #
#                                                      :::      ::::::::   #
#   ft_garden_security.py                            ::+::    :+:    :+:   #
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
        self._height = 0.0
        self._age = 0
        self.set_height(my_height)
        self.set_age(my_age)

    # --- GETTERS ---
    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    # --- SETTERS ---
    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = float(new_height)

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = int(new_age)

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")

# --- PRUEBA DEL SISTEMA DE SEGURIDAD ---


def security_test() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    rose.set_height(25)
    print("\nHeight updated: 25cm")
    rose.set_age(30)
    print("Age updated: 30 days")
    rose.set_height(-5)
    rose.set_age(-1)
    print("\nCurrent state: ", end="")
    rose.show()


if __name__ == "__main__":
    security_test()
