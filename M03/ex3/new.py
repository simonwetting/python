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
		print(f"{PLAYERS[n]}")
	

if __name__ == "__main__":
	main()