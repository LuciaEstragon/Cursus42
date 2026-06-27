#!/usr/bin/env python3
"""
Exercise 0: Lambda Sanctum
Master anonymous functions with lambda expressions.
"""


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """
    Sort artifacts by power descending using sorted() and a lambda.
    """
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """
    Filter mages with power >= min_power using filter() and a lambda.
    """
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """
    Transform spell names with ** prefix and suffix using map() and lambda.
    """
    return list(map(lambda s: f"**{s}**", spells))


def mage_stats(mages: list[dict]) -> dict:
    """
    Calculate max, min and average power using lambdas with max/min.
    """
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}

    max_power = max(mages, key=lambda m: m['power'])['power']
    min_power = min(mages, key=lambda m: m['power'])['power']
    avg_power = round(sum(m['power'] for m in mages) / len(mages), 2)
    return {
        'max_power': max_power, 'min_power': min_power, 'avg_power': avg_power
        }


if __name__ == "__main__":
    # Sample data
    artifacts = [
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'},
        {'name': 'Crystal Orb', 'power': 85, 'type': 'focus'},
        {'name': 'Shadow Cloak', 'power': 78, 'type': 'armor'},
        {'name': 'Lightning Rod', 'power': 95, 'type': 'weapon'},
    ]

    mages = [
        {'name': 'Gandalf', 'power': 90, 'element': 'fire'},
        {'name': 'Merlin', 'power': 75, 'element': 'water'},
        {'name': 'Morgana', 'power': 88, 'element': 'shadow'},
        {'name': 'Radagast', 'power': 60, 'element': 'earth'},
    ]

    spells = ['fireball', 'heal', 'shield', 'teleport']

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    for a in sorted_artifacts[:4]:
        print(f"{a['name']} ({a['power']} power) comes before ...")

    print("\nTesting power_filter...")
    filtered = power_filter(mages, 80)
    for m in filtered:
        print(f"{m['name']} has power {m['power']}")

    print("\nTesting spell transformer...")
    print(" ".join(spells))
    transformed = spell_transformer(spells)
    print(" ".join(transformed))

    print("\nTesting mage_stats...")
    stats = mage_stats(mages)
    print(f"Max power: {stats['max_power']}, Min power: {stats['min_power']}, "
          f"Avg power: {stats['avg_power']}")
