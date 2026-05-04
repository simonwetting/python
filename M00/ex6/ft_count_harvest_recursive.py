def recurse(days):
    if days > 1:
        recurse(days - 1)
    print(f"Day {days}")


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    recurse(days)
