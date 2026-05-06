import random
from typing import Generator


PLAYERS = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
ACTIONS = ["jumped", "ran", "slept", "ate", "danced"]


def generate() -> Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(PLAYERS), random.choice(ACTIONS))


def consume_event(
    events: list[tuple[str, str]],
) -> Generator[tuple[str, str], None, None]:
    while events:
        item = random.choice(events)
        events.remove(item)
        yield item


def main() -> None:
    gen = generate()

    for i in range(1, 1001):
        name, action = next(gen)
        print(f"Event {i}: Player {name} did action {action}")

    events = [next(gen) for _ in range(10)]
    print(events)

    for event in consume_event(events):
        print(event)
        print(events)


if __name__ == "__main__":
    main()
