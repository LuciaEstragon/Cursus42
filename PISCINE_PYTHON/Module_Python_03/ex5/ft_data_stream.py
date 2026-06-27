#!/usr/bin/env python3

# ************************************************************************ #
#                                                                          #
#                                                      :::      ::::::::   #
#   ft_data_stream.py                                ::+::    :+:    :+:   #
#                                                  +:+ +:+         +:+     #
#   By: lestrada <lestrada@student.42.es>        +#+  +:+       +#+        #
#                                              +#+#+#+#+#+   +#+           #
#   Created: 2026/05/06          by lestrada        #+#    #+#             #
#   Updated: 2026/05/10          by lestrada       ###   ########.es       #
#                                                                          #
# ************************************************************************ #


import random
from typing import Generator, Tuple


NAMES = ["Harry", "Ron", "Hermione", "Draco", "Luna", "Neville"]
ACTIONS = ["Alohomora", "Expecto Patronum", "Expelliarmus", "Accio",
           "Wingardium Leviosa", "Protego", "Reparo", "Lumus"]


def gen_event() -> Generator[Tuple[str, str], None, None]:
    while True:
        yield (random.choice(NAMES), random.choice(ACTIONS))


def consume_event(event_list: list[Tuple[str, str]]
                  ) -> Generator[Tuple[str, str], None, None]:
    while event_list:
        idx = random.randint(0, len(event_list)-1)
        yield event_list.pop(idx)


def main() -> None:
    # 1000 eventos del generador infinito
    generator1 = gen_event()
    print("=== Game Data Stream Processor ===")
    for ind in range(1000):
        event1 = next(generator1)
        print(f"Event {ind}: Player {event1[0]} did {event1[1]}")

    # Lista de 10 eventos
    generator2 = gen_event()
    event2 = [next(generator2) for _ in range(10)]
    print("\n=== Built list of 10 events: ===")
    print(event2)
    print()
    # for e in event2:
    #     print(e)

    # Consumir aleatoriamente
    print("\n=== Consuming events randomly ===")
    for event in consume_event(event2):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event2}")
    print("No more events.")


if __name__ == "__main__":
    main()
