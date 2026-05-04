def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type = seed_type[0].upper() + seed_type[1:]
    print(f"{seed_type} seeds {quantity} {unit} available")
