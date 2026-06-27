# ************************************************************************ #
#                                                                          #
#                                                      :::      ::::::::   #
#   ft_plant_age.py                                  ::+::    :+:    :+:   #
#                                                  +:+ +:+         +:+     #
#   By: lestrada <lestrada@student.42.es>        +#+  +:+       +#+        #
#                                              +#+#+#+#+#+   +#+           #
#   Created: 2026/04/02 09:30:00 by lestrada        #+#    #+#             #
#   Updated: 2026/04/02 09:30:00 by lestrada       ###   ########.es       #
#                                                                          #
# ************************************************************************ #

def ft_plant_age() -> None:
    day = int(input("Enter plant age in days:"))
    if day > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
