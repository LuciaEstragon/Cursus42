#!/usr/bin/env python3

# ************************************************************************ #
#                                                                          #
#                                                      :::      ::::::::   #
#   ft_achievement_tracker.py                        ::+::    :+:    :+:   #
#                                                  +:+ +:+         +:+     #
#   By: lestrada <lestrada@student.42.es>        +#+  +:+       +#+        #
#                                              +#+#+#+#+#+   +#+           #
#   Created: 2026/05/06          by lestrada        #+#    #+#             #
#   Updated: 2026/05/10          by lestrada       ###   ########.es       #
#                                                                          #
# ************************************************************************ #


import random


ALL_ACHIEVEMENTS = [
    "First Blood", "Double Kill", "Triple Kill", "Head Hunter", "Guardian",
    "Treasure Hunter", "Speed Run", "Flawless Victory", "Berserker",
    "Sharpshooter", "Mage", "Warrior", "Healer", "Assassin", "Tank",
    "Explorer", "Crafter", "Merchant", "Lucky", "Untouchable"
]


def gen_player_achievements() -> set[str]:
    num = random.randint(3, 10)
    selected = random.sample(ALL_ACHIEVEMENTS, num)
    return set(selected)


def main() -> None:
    print(f"=== Achievement Tracker System ===\n")

    player_names = ["Alice", "Bob", "Charlie", "Dylan"]
    players = [gen_player_achievements() for _ in range(4)]
    for name, ach in zip(player_names, players):
        print(f"Player {name}: {ach}")

    all_achievements = set.union(*players)
    common_all = set.intersection(*players)
    print("\nAll distinct achievements:", all_achievements)
    print(f"Common achievements: {common_all if common_all else 'none'}")

    for i, (name, ach) in enumerate(zip(player_names, players)):
        others_union = set.union(
            *[p for j, p in enumerate(players) if j != i]
        )
        exclusive = ach - others_union
        print(f"Only {name} has: {exclusive if exclusive else set()}")

    for name, ach in zip(player_names, players):
        missing = all_achievements - ach
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()
