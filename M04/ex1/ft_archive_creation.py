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
    except Exception as e:
        print(f"Error opening file '{path}': {e}")
    else:
        content = content.replace("\n", "#\n") + "#"
        print(f"---\n\n{content}\n\nFile 'ancient_fragment.txt'closed."
              f"\n\nTransform data:\n---\n\n{content}\n\n---")
        file.close()
        filename = input(f"Enter new file name (or empty): ")
        if filename:
            


if __name__ == "__main__":
    main()
