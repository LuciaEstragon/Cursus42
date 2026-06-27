# ************************************************************************ #
#                                                                          #
#                                                      :::      ::::::::   #
#   ft_water_reminder.py                             ::+::    :+:    :+:   #
#                                                  +:+ +:+         +:+     #
#   By: lestrada <lestrada@student.42.es>        +#+  +:+       +#+        #
#                                              +#+#+#+#+#+   +#+           #
#   Created: 2026/04/02 09:30:00 by lestrada        #+#    #+#             #
#   Updated: 2026/04/02 09:30:00 by lestrada       ###   ########.es       #
#                                                                          #
# ************************************************************************ #

def ft_water_reminder() -> None:
    day = int(input("Days since last watering:"))
    if day > 2:
        print("Water the plants!")
    else:
        print("Plants are fine.")
