import random
from typing import Generator


PLAYERS = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
ACTIONS = ["jumped", "ran", "slept", "ate", "danced"]


def generate() -> Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(PLAYERS), random.choice(ACTIONS))


def lst_to_str(lst: list[tuple[str, str]]) -> str:
    string_list = str()
    for name, action in lst:
        string_list += f"('{name}', '{action}'), "
    string_list = string_list[:-2]
    return string_list


def main() -> None:
    gen = generate()
    for n in range(0, 1000):
        name, action = next(gen)
        print(f"Event {n}: Player {name} did action {action}")
    lst: list[tuple[str, str]] = []
    for n in range(10):
        lst.append(next(gen))
    print(f"Built list of 10 events: [{lst_to_str(lst)}]")
    for _ in range(10):
        player, action = lst.pop()
        print(f"[({player}, {action})]")
        print(f"Remains in list: [{lst_to_str(lst)}]")


if __name__ == "__main__":
    main()
