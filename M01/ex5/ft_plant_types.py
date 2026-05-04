#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float = 1.0) -> None:
        self.__name = name
        self.__height = height if height >= 0 else 0.0
        self.__age = age if age >= 0 else 0
        self.__growth_rate = growth_rate

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

    def age(self) -> None:
        self.__age += 1

    def show(self) -> None:
        print(f"{self.__name}: {round(self.__height, 1)}cm, "
              f"{self.__age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
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

    def produce_shade(self) -> None:
        print(
            f"Tree {self.get_name()} now produces a shade of "
            # f"{round(self.get_height(), 1)}cm long and "
            # f"{self.get_height()}cm long and "
            f"{self._Plant__height}cm long and "
            f"{self.__trunk_diameter}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.__trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, growth_rate: float = 1.0) -> None:
        super().__init__(name, height, age, growth_rate)
        self.__harvest_season = harvest_season
        self.__nutritional_value: int = 0

    def grow(self) -> None:
        super().grow()
        self.__nutritional_value += 1

    def age(self) -> None:
        super().age()
        self.__nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.__harvest_season}")
        print(f"Nutritional value: {self.__nutritional_value}")


def main() -> None:
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April", 2.1)
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()


if __name__ == "__main__":
    main()
