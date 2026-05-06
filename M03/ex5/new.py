import random
from typing import Generator


PLAYERS = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
ACTIONS = ["jumped", "ran", "slept", "ate", "danced"]


def generate() -> Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(PLAYERS), random.choice(ACTIONS))


# def consume_event():


def main() -> None:
    gen  = generate()
    for n in range(0, 1000):
        name, action = next(gen)
        print(f"Event {n}: Player {name} did action {action}")
    lst: list[tuple[str, str]] = []
    for n in range(10):
        lst.append(next(gen))
    string_list = str()
    for name, action in lst:
        string_list += f"('{name}', '{action}'),"
    string_list = string_list[:-1]
    print(string_list)
    
    for _ in range(10):
        s, comma, last_part = s.rpartition(",")
        
        print(f"Got event")
    # for name, action in lst:
    #     print(f"Got event from list: Player {name} did action {action}")

if __name__ == "__main__":
    main()
