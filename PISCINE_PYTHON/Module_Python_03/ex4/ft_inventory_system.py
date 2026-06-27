#!/usr/bin/env python3

# ************************************************************************ #
#                                                                          #
#                                                      :::      ::::::::   #
#   ft_inventory_system.py                           ::+::    :+:    :+:   #
#                                                  +:+ +:+         +:+     #
#   By: lestrada <lestrada@student.42.es>        +#+  +:+       +#+        #
#                                              +#+#+#+#+#+   +#+           #
#   Created: 2026/05/06          by lestrada        #+#    #+#             #
#   Updated: 2026/05/10          by lestrada       ###   ########.es       #
#                                                                          #
# ************************************************************************ #

import sys


def main() -> None:
    inventory = {}
    order = []
    for arg in sys.argv[1:]:
        if ':' not in arg:
            print(f"Invalid format (no colon): {arg}")
            continue
        parts = arg.split(':', 1)
        name = parts[0].strip()
        qty_str = parts[1].strip()
        try:
            qty = int(qty_str)
        except ValueError:
            print(f"Invalid quantity (not an integer): {arg}")
            continue
        if name in inventory:
            print(f"Redundant item, skipped: {arg}")
            continue
        inventory[name] = qty
        order.append(name)

    if not inventory:
        print("No valid items.")
        return

    print("=== Inventory ===")
    for name in order:
        print(f"{name}: {inventory[name]}")

    # items_list = list(inventory.keys())
    total_qty = sum(inventory.values())
    print(f"\nTotal items count: {total_qty}")
    print("Percentage of each item:")
    for name in order:
        percent = (inventory[name] / total_qty) * 100
        print(f"{name}: {percent:.1f}%")

    # Most abundant (max)
    max_item = None
    max_qty = -1
    for name in order:
        q = inventory[name]
        if q > max_qty:
            max_qty = q
            max_item = name

    # Least abundant (min)
    min_item = None
    min_qty = float('inf')
    for name in order:
        q = inventory[name]
        if q < min_qty:
            min_qty = q
            min_item = name

    print(f"\nMost abundant: {max_item} ({max_qty})")
    print(f"Least abundant: {min_item} ({min_qty})")

    # Add a new item
    new_item = "Coin"
    new_qty = 100
    inventory[new_item] = new_qty
    order.append(new_item)
    print(f"\n=== Inventory after adding {new_item} ===")
    for name in order:
        print(f"{name}: {inventory[name]}")


if __name__ == "__main__":
    main()
