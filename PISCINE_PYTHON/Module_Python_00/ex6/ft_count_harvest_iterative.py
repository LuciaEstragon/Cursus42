# ************************************************************************ #
#                                                                          #
#                                                      :::      ::::::::   #
#   ft_count_harvest_iterative.py                    ::+::    :+:    :+:   #
#                                                  +:+ +:+         +:+     #
#   By: lestrada <lestrada@student.42.es>        +#+  +:+       +#+        #
#                                              +#+#+#+#+#+   +#+           #
#   Created: 2026/04/02 09:30:00 by lestrada        #+#    #+#             #
#   Updated: 2026/04/02 09:30:00 by lestrada       ###   ########.es       #
#                                                                          #
# ************************************************************************ #

def ft_count_harvest_iterative() -> None:
    day = int(input("Days until harvest:"))
    i = 1
    while day > 0:
        print(f"Day {i}")
        day -= 1
        i += 1
    print("Harvest time!")
