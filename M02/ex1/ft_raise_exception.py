def input_temperature(temperature: str) -> int:
    return int(temperature)


def test_temperature():
    print("=== Garden Temperature ===")
    for temp_str in ["25", "100", "abc", "-50"]:
        try:
            temp = input_temperature(temp_str)
            if (temp < 0 or temp > 40):
                raise ValueError("Temperature out of range")
            print(f"Temperature is now {temp}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
