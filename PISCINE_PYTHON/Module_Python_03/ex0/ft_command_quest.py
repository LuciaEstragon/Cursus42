#!/usr/bin/env python3

# ************************************************************************ #
#                                                                          #
#                                                      :::      ::::::::   #
#   ft_command_quest.py                              ::+::    :+:    :+:   #
#                                                  +:+ +:+         +:+     #
#   By: lestrada <lestrada@student.42.es>        +#+  +:+       +#+        #
#                                              +#+#+#+#+#+   +#+           #
#   Created: 2026/05/06          by lestrada        #+#    #+#             #
#   Updated: 2026/05/10          by lestrada       ###   ########.es       #
#                                                                          #
# ************************************************************************ #


import sys


def main() -> None:
    args = sys.argv
    prog_name = args[0]
    other_args = args[1:]
    num_other = len(other_args)

    print("== Command Quest ==")
    print(f"Program name: {prog_name}")

    if num_other == 0:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {num_other}")
        for i, arg in enumerate(other_args, start=1):
            print(f"Argument {i}: {arg}")
    print(f"Total arguments: {len(args)}")


if __name__ == "__main__":
    main()
