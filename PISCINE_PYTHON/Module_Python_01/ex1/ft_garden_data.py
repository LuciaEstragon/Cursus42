#!/usr/bin/env python3

# ************************************************************************ #
#                                                                          #
#                                                      :::      ::::::::   #
#   ft_garden_data.py                                ::+::    :+:    :+:   #
#                                                  +:+ +:+         +:+     #
#   By: lestrada <lestrada@student.42.es>        +#+  +:+       +#+        #
#                                              +#+#+#+#+#+   +#+           #
#   Created: 2026/04/02 09:30:00 by lestrada        #+#    #+#             #
#   Updated: 2026/04/27 09:30:00 by lestrada       ###   ########.es       #
#                                                                          #
# ************************************************************************ #

class Plant:
    def __init__(self, my_name: str, my_height: int, my_age: int) -> None:
        self.name = my_name
        self.height = my_height
        self.age = my_age

    def show(self) -> None:
        print(f"Plant: {self.name} \n" +
              f"Height: {self.height}cm \n" +
              f"Age: {self.age} days old \n ")


def main() -> None:
    print("=== Welcome to My Garden ===")
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)
    plant1.show()
    plant2.show()
    plant3.show()
    print("=== End of Program ===")


if __name__ == "__main__":
    main()
