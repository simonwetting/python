import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        raw = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = raw.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        try:
            x, y, z = float(parts[0]), float(parts[1]), float(parts[2])
            return (x, y, z)
        except ValueError as e:
            for part in parts:
                try:
                    float(part)
                except ValueError:
                    print(f"Error on parameter '{part.strip()}': {e}")
                    break
 
def distance(p1: tuple[float, float, float], p2: tuple[float, float, float]) ->float:
    return math.sqrt((p1[0] - p2[0]) **2
                     + (p1[1] - p2[1]) **2
                     + (p1[2] - p2[2]) **2)

def main() -> None:
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    print(f"Distance to center: {round(distance(pos1, (0.0, 0.0, 0.0)), 4)}")

    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    print(f"Distance between the 2 sets of coordinates: "
          f"{round(distance(pos1, pos2), 4)}")


if __name__ == "__main__":
    main()
