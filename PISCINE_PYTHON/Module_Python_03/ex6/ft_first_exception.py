#!/usr/bin/env python3

# ************************************************************************ #
#                                                                          #
#                                                      :::      ::::::::   #
#   ft_first_exception.py                            ::+::    :+:    :+:   #
#                                                  +:+ +:+         +:+     #
#   By: lestrada <lestrada@student.42.es>        +#+  +:+       +#+        #
#                                              +#+#+#+#+#+   +#+           #
#   Created: 2026/05/06          by lestrada        #+#    #+#             #
#   Updated: 2026/05/10          by lestrada       ###   ########.es       #
#                                                                          #
# ************************************************************************ #

import random


NAMES = ["aRagorn", "Legolas", "GIMLI", "Frodo", "sam", "GANDALF", "arWeN"]


def capitalizer_case(list_name: list[str]) -> list[str]:
    return [name[0].upper() + name[1:].lower() for name in list_name]


def are_capitalizer(list_name: list[str]) -> list[str]:
    return [name for name in list_name if name.istitle()]
    # return [name for name in list_name if name.isupper()]
    # return [name for name in list_name if name.islower()]


def main() -> None:
    print("=== Game Data Archemist===")
    original_names = NAMES
    print("Initial names of players:", original_names)

    # primera letra mayúscula
    names_capitalizer = capitalizer_case(original_names)
    print(f"New list with all names capitalized: {names_capitalizer}")

    # filtrar nombres ya en mayúsculas en la lista original
    already_cap = are_capitalizer(original_names)
    print(f"New list of capitalized names only: {already_cap}")

    # diccionario con nombres normalizados + media + los mejores
    scores_dict = {
        name: random.randint(50, 200) for name in names_capitalizer
    }
    print(f"Score dict: {scores_dict}")
    avg = sum(scores_dict.values()) / len(scores_dict)
    print(f"Score average is {avg:.2f}")
    high_performers = {
        name: score for name, score in scores_dict.items() if score > avg
    }
    # print(f"High scores: {high_performers}")

    # extra : los he ordenado
    score_sort = [(score, name) for name, score in high_performers.items()]
    score_sort.sort(reverse=True)  # orden descendente : al reves False
    sorted_by_score = [(name, score) for score, name in score_sort]
    print(f"High scores: {sorted_by_score}")


if __name__ == "__main__":
    main()
