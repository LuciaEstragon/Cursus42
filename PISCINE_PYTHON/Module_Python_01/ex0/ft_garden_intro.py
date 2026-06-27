#!/usr/bin/env python3

# ************************************************************************ #
#                                                                          #
#                                                      :::      ::::::::   #
#   ft_garden_intro.py                               ::+::    :+:    :+:   #
#                                                  +:+ +:+         +:+     #
#   By: lestrada <lestrada@student.42.es>        +#+  +:+       +#+        #
#                                              +#+#+#+#+#+   +#+           #
#   Created: 2026/04/02 09:30:00 by lestrada        #+#    #+#             #
#   Updated: 2026/04/27 09:30:00 by lestrada       ###   ########.es       #
#                                                                          #
# ************************************************************************ #

def display_info(name: str, height: int, age: int) -> None:
    print(f"Plant: {name} \n" +
          f"Height: {height} cm \n" +
          f"Age: {age} days \n ")


def main() -> None:
    print("=== Welcome to My Garden ===")
    display_info("Rose", 25, 30)
    print("=== End of Program ===")


if __name__ == "__main__":
    main()
