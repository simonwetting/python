#!/usr/bin/env python3


class Plant:
    class Stats:
        def __init__(self) -> None:
            self.__grow_count: int = 0
            self.__age_count: int = 0
            self.__show_count: int = 0

        def increment_grow(self) -> None:
            self.__grow_count += 1

        def increment_age(self) -> None:
            self.__age_count += 1

        def increment_show(self) -> None:
            self.__show_count += 1

        def display(self) -> None:
            print(
                f"Stats: {self.__grow_count} grow, "
                f"{self.__age_count} age, "
                f"{self.__show_count} show"
            )

    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float = 1.0) -> None:
        self.__name = name
        self.__height = height if height >= 0 else 0.0
        self.__age = age if age >= 0 else 0
        self.__growth_rate = growth_rate
        self.__stats = Plant.Stats()

    def get_name(self) -> str:
        return self.__name

    def get_height(self) -> float:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.__name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self.__height = height
        print(f"Height updated: {height:g}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.__name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self.__age = age
        print(f"Age updated: {age} days")

    def grow(self) -> None:
        self.__height += self.__growth_rate
        self.__stats.increment_grow()

    def age(self) -> None:
        self.__age += 1
        self.__stats.increment_age()

    def show(self) -> None:
        print(
            f"{self.__name}: {round(self.__height, 1)}cm, "
            f"{self.__age} days old"
        )
        self.__stats.increment_show()

    def show_stats(self) -> None:
        self.__stats.display()

    @staticmethod
    def is_older_than_a_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> 'Plant':
        return cls("Unknown plant", 0.0, 0)

    @classmethod
    def convert_to_flower(cls, obj: 'Plant') -> 'Flower':
        return cls(obj.get_name(), obj.get_height(), obj.get_age(), "unknown")

    @classmethod
    def convert_to_tree(cls, obj: 'Plant') -> 'Tree':
        return cls(obj.get_name(), obj.get_height(),
                   obj.get_age(), obj.get_age() * 0.1)

    @classmethod
    def convert_to_vegetable(cls, obj: 'Plant') -> 'Vegetable':
        return cls(obj.get_name(), obj.get_height(), obj.get_age())


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 color: str, growth_rate: float = 1.0) -> None:
        super().__init__(name, height, age, growth_rate)
        self.__color = color
        self.__bloomed = False

    def bloom(self) -> None:
        self.__bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.__color}")
        if self.__bloomed:
            print(f"{self.get_name()} is blooming beautifully!")
        else:
            print(f"{self.get_name()} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.__trunk_diameter = trunk_diameter
        self.__shade_count: int = 0

    def produce_shade(self) -> None:
        self.__shade_count += 1
        print(
            f"Tree {self.get_name()} now produces a shade of "
            f"{round(self.get_height(), 1)}cm long and "
            f"{self.__trunk_diameter}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.__trunk_diameter}cm")

    def show_stats(self) -> None:
        super().show_stats()
        print(f"{self.__shade_count} shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str = "summer",
                 growth_rate: float = 1.0) -> None:
        super().__init__(name, height, age, growth_rate)
        self.__harvest_season = harvest_season
        self.__nutritional_value: int = 0

    def grow(self) -> None:
        super().grow()
        self.__nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.__harvest_season}")
        print(f"Nutritional value: {self.__nutritional_value}")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int,
                 color: str, seeds: int, growth_rate: float = 1.0) -> None:
        super().__init__(name, height, age, color, growth_rate)
        self.__seeds = seeds
        self.__revealed_seeds: int = 0

    def bloom(self) -> None:
        super().bloom()
        self.__revealed_seeds = self.__seeds

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.__revealed_seeds}")


def display_stats(plant: Plant) -> None:
    plant.show_stats()


def main() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_a_year(30)}")
    print(
        f"Is 400 days more than a year? -> {Plant.is_older_than_a_year(400)}"
    )

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red", growth_rate=8.0)
    rose.show()
    print("[statistics for Rose]")
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    display_stats(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[statistics for Oak]")
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    display_stats(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow", 42, growth_rate=1.5)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    for _ in range(20):
        sunflower.grow()
        sunflower.age()
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    display_stats(sunflower)

    print("\n=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    print("[statistics for Unknown plant]")
    display_stats(anonymous)


if __name__ == "__main__":
    main()
