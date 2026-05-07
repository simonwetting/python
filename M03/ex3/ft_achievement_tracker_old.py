import random

ACHIEVEMENTS: list[str] = [
    "Crafting Genius", "World Savior", "Master Explorer",
    "Collector Supreme", "Untouchable", "Boss Slayer",
    "Strategist", "Unstoppable", "Speed Runner", "Survivor",
    "Treasure Hunter", "First Steps", "Sharp Mind", "Hidden Path Finder"
]

PLAYERS: list[str] = ["Alice", "Bob", "Charlie", "Dylan"]


def gen_player_achievements() -> set[str]:
    count = random.randint(5, 9)
    return set(random.sample(ACHIEVEMENTS, count))


def main() -> None:
    print("=== Achievement Tracker System ===")

    names: list[str] = []
    ach_sets: list[set[str]] = []
    for player in PLAYERS:
        names.append(player)
        ach_sets.append(gen_player_achievements())

    for i in range(len(names)):
        print(f"Player {names[i]}: {ach_sets[i]}")

    all_distinct: set[str] = set(ach_sets[0])
    common: set[str] = set(ach_sets[0])
    for i in range(1, len(ach_sets)):
        all_distinct = set.union(all_distinct, ach_sets[i])
        common = set.intersection(common, ach_sets[i])

    print(f"All distinct achievements: {all_distinct}")
    print(f"Common achievements: {common}")

    for i in range(len(names)):
        others: set[str] = set()
        for j in range(len(names)):
            if j != i:
                others = set.union(others, ach_sets[j])
        only = set.difference(ach_sets[i], others)
        if not only:
            print(f"Only {names[i]} has: {only}")
        print(f"{names[i]} has nothing unique")

    full_set = set(ACHIEVEMENTS)
    for i in range(len(names)):
        missing = set.difference(full_set, ach_sets[i])
        print(f"{names[i]} is missing: {missing}")


if __name__ == "__main__":
    main()
