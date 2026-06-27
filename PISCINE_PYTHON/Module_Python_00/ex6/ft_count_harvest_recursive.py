# ************************************************************************ #
#                                                                          #
#                                                      :::      ::::::::   #
#   ft_count_harvest_recursive.py                    ::+::    :+:    :+:   #
#                                                  +:+ +:+         +:+     #
#   By: lestrada <lestrada@student.42.es>        +#+  +:+       +#+        #
#                                              +#+#+#+#+#+   +#+           #
#   Created: 2026/04/02 09:30:00 by lestrada        #+#    #+#             #
#   Updated: 2026/04/02 09:30:00 by lestrada       ###   ########.es       #
#                                                                          #
# ************************************************************************ #

def ft_count_harvest_recursive() -> int:
    day = int(input("Days until harvest: "))

    def aux(current: int) -> int:
        if current > day:
            print("Harvest time!")
            return 0
        print(f"Day {current}")
        return 1 + aux(current + 1)
    return aux(1)
