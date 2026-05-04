#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.__name = name
        self.__height = height if height >= 0 else 0.0
        self.__age = age if age >= 0 else 0

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

    def show(self) -> None:
        print(f"{self.__name}: {self.__height}cm, {self.__age} days old")


def main() -> None:
    rose = Plant("Rose", 15.0, 10)

    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    rose.show()
    rose._Plant__name = "test"

    rose.set_height(25.0)
    rose.set_age(30)
    rose.set_height(-5.0)
    rose.set_age(-10)

    print("Current state: ", end="")
    rose.show()


if __name__ == "__main__":
    main()
