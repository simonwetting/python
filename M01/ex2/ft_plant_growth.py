#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int, growth: int):
        self.name = name
        self.height = height
        self.age = age
        self.growth = growth

    def show(self):
        print(f"{self.name}: {self.height:.2f}cm, {self.age} days old")

    def grow(self):
        self.height = self.height + self.growth
        self.age += 1

# def age_plants(n: int, day: int):
#    rose.show()
#    sunflower.show()
#    cactus.show()


def main():
    rose = Plant("Rose", 25, 30, 0.1)
    sunflower = Plant("Sunflower", 80, 45, 0.3)
    cactus = Plant("Cactus", 15, 120, 0.01)
    print("=== Garden Plant Registry ===")

    n = 1
    while (n <= 7):
        print(f"=== Day {n} ===")
        rose.show()
        sunflower.show()
        cactus.show()
        rose.grow()
        sunflower.grow()
        cactus.grow()
        n += 1


if __name__ == "__main__":
    main()
