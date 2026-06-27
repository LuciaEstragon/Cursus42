# ************************************************************************ #
#                                                                          #
#                                                      :::      ::::::::   #
#   ft_harvest_total.py                              :+:      :+:    :+:   #
#                                                  +:+ +:+         +:+     #
#   By: lestrada <lestrada@student.42.es>        +#+  +:+       +#+        #
#                                              +#+#+#+#+#+   +#+           #
#   Created: 2026/04/02 09:30:00 by lestrada        #+#    #+#             #
#   Updated: 2026/04/02 09:30:00 by lestrada       ###   ########.es       #
#                                                                          #
# ************************************************************************ #

def ft_harvest_total() -> None:
    i = 0
    result = 0
    while i < 3:
        day = int(input(f"Day {i + 1} harvest: "))
        result += day
        i += 1
    print(f"Total harvest: {result}")


"""
def ft_harvest_total_other():
    day1 = int(input("Day 1 harvest:"))
    print(day1)
    day2 = int(input("Day 2 harvest:"))
    print(day2)
    day3 = int(input("Day 3 harvest:"))
    print(day3)
    total = day1 + day2 + day3
    print(f"Total harvest: {total}")
"""
