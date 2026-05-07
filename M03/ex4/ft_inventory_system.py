import sys


def main() -> None:
    args = sys.argv[1:]
    inventory: dict[str, int] = {}
    distinct_items = 0
    for arg in args:
        if ":" not in arg:
            print("skipping arg without :")
            continue
        tmp = arg.split(":", 1)
        try:
            item: tuple[str, int] = (tmp[0], int(tmp[1]))
        except ValueError as e:
            print(f"{tmp[0]} {e}")
        else:
            distinct_items += 1
        exists = item in inventory
        if not exists:
            inventory[item[0]] = item[1]
        else:
            inventory.get(item[0]) + item[1]
    print("=== Your Inventory ===")
    total: int = sum(quantity for name, quantity in inventory)
    print(f"Total quantity of the {distinct_items} items: {total}")
    for name, quantity in inventory:
        print(f"Item {name} represents {round(float(100 * quantity/total), 3)}%")

# def main() -> None:
# args = sys.argv[1:]
# inventory: list[tuple[str, int]] = []
# distinct_items = 0
# for arg in args:
# if ":" not in arg:
# print("skipping arg without :")
# continue
# tmp = arg.split(":", 1)
# try:
# item: tuple[str, int] = (tmp[0], int(tmp[1]))
# except ValueError as e:
# print(f"{tmp[0]} {e}")
# else:
# distinct_items += 1
# inventory.append(item)
# print("=== Your Inventory ===")
# total: int = sum(quantity for name, quantity in inventory)
# print(f"Total quantity of the {distinct_items} items: {total}")
# for name, quantity in inventory:
# print(f"Item {name} represents {round(float(100 * quantity/total), 3)}%")


if __name__ == "__main__":
    main()
