# ************************************************************************ #
#                                                                          #
#                                                      :::      ::::::::   #
#   ft_seed_inventory.py                             ::+::    :+:    :+:   #
#                                                  +:+ +:+         +:+     #
#   By: lestrada <lestrada@student.42.es>        +#+  +:+       +#+        #
#                                              +#+#+#+#+#+   +#+           #
#   Created: 2026/04/02 09:30:00 by lestrada        #+#    #+#             #
#   Updated: 2026/04/02 09:30:00 by lestrada       ###   ########.es       #
#                                                                          #
# ************************************************************************ #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    print(f"{seed_type} seeds: {quantity} ", end=" ")
    if unit == "packets":
        print("packets available")
    elif unit == "grams":
        print("grams total")
    elif unit == "area":
        print("square meters")
    else:
        print("Unknown unit type")
