import sys

def main() -> None:
	args = sys.argv[1:]
	inventory: list[tuple[str, int]] = []
	for arg in args:
		if ":" not in arg:
			print("skipping arg without :")
			continue
		tmp = arg.split(":", 1)
		try:
			item: tuple[str, int] = (tmp[0], int(tmp[1]))
		except:
			print(f"{tmp[0]} has an invalid value")
		inventory.append(item)
	for name, quantity in inventory:
		print(f"{quantity} times {name}")

# import sys

# def main() -> None:
#     args = sys.argv[1:]
#     inventory: list[tuple[str, int]] = []

#     for arg in args:
#         if ":" not in arg:
#             print(f"Skipping invalid: {arg}")
#             continue
#         tmp = arg.split(":", 1)
#         name = tmp[0].strip()
#         try:
#             quantity = int(tmp[1].strip())
#             inventory.append((name, quantity))
#         except ValueError:
#             print(f"Skipping invalid quantity: {arg}")

#     print("=== Your Inventory ===")
#     for name, quantity in inventory:
#         print(f"{quantity} times {name}")


if __name__ == "__main__":
    main()