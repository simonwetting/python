import sys

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        path = sys.argv[1]
    print(f"=== Cyber Archives Recovery ===\nAccessing file '{path}'")
    try:
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
    # except FileNotFoundError as e:
    #     print(f"Error opening file '{path}': {e}")
    # except PermissionError as e:
    #     print(f"Error opening file '{path}': {e}")
    except Exception as e:
        print(f"Error opening file '{path}': {e}")
    else:
        print(f"---\n\n{content}")

if __name__ == "__main__":
    main()