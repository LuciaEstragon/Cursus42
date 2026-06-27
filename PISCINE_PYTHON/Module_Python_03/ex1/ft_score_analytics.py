#!/usr/bin/env python3

# ************************************************************************ #
#                                                                          #
#                                                      :::      ::::::::   #
#   ft_score_analytics.py                            ::+::    :+:    :+:   #
#                                                  +:+ +:+         +:+     #
#   By: lestrada <lestrada@student.42.es>        +#+  +:+       +#+        #
#                                              +#+#+#+#+#+   +#+           #
#   Created: 2026/05/06          by lestrada        #+#    #+#             #
#   Updated: 2026/05/10          by lestrada       ###   ########.es       #
#                                                                          #
# ************************************************************************ #

import sys


def main() -> None:
    raw_args = sys.argv[1:]
    scores = []

    for arg in raw_args:
        try:
            score = float(arg)
            scores.append(score)
        except ValueError:
            print(f"Invalid parameters: {arg}")

    if not scores:
        print("No valid scores provided.")
        return

    total = sum(scores)
    count = len(scores)
    avg = total / count
    max_score = max(scores)
    min_score = min(scores)
    range_score = max_score - min_score

    print("=== Player Score Analytics ===")
    print(f"Total players: {count}")
    print(f"Total scores: {total}")
    print(f"Average score: {avg:.2f}")
    print(f"High score: {max_score}")
    print(f"Low score: {min_score}")
    print(f"Score range: {range_score}")


if __name__ == "__main__":
    main()
