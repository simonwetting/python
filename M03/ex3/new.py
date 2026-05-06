import random

ACHIEVEMENTS: list[str] = [
	"Crafting Genius", "World Savior", "Master Explorer",
    "Collector Supreme", "Untouchable", "Boss Slayer",
    "Strategist", "Unstoppable", "Speed Runner", "Survivor",
    "Treasure Hunter", "First Steps", "Sharp Mind", "Hidden Path Finder"]

PLAYERS: list[str] = ["Alice", "Bob", "Charlie", "Dylan"]


def gen_achievements() -> set[str]:
	count = random.randint(5, 9)
	return set(random.sample(ACHIEVEMENTS, count))


def main() -> None:
    ach_sets: list[set[str]] = []
    for _ in PLAYERS:
        ach_sets.append(gen_achievements())
    for n in range(0, len(PLAYERS)):
        print(f"Player {PLAYERS[n]}: {ach_sets[n]}")
    distinct: set[str] = set(ach_sets[0])
    common: set[str] = set(ach_sets[0])
    for n in range(1, len(ach_sets)):
        distinct = set.union(distinct, ach_sets[n])
        common = set.intersection(distinct, ach_sets[n])
    print(f"\nAll distinct achievements: {distinct}")
    print(f"\nCommon achievements: {common}\n")
    for n in range(0, len(PLAYERS)):
        others: set[str] = set()
        for m in range(0, len(PLAYERS)):
            if n != m:
                others = set.union(others, ach_sets[m])
        unique = set.difference(ach_sets[n], others)
        print(f"Only {PLAYERS[n]} has {unique}")
    print("\n")
    for n in range(0, len(PLAYERS)):
        missing = set.difference(set(ACHIEVEMENTS), ach_sets[n])
        print(f"{PLAYERS[n]} is missing {missing}")

if __name__ == "__main__":
	main()