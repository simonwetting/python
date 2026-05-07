import random

PLAYERS: list[str] = ['Alice', 'bob', 'Charlie', 'dylan',
                      'Emma', 'Gregory', 'john', 'kevin', 'Liam']


def print_list(lst: list[str]) -> None:
    strlst = str()
    for player in lst:
        strlst += f"'{player}', "
    strlst = strlst[:-2]
    print(f"[{strlst}]")


def print_scores(dct: dict[str, int]) -> None:
    strlst = str()
    for player, score in dct:
        strlst += f"{player}: {score}, "
    strlst = strlst[:-2]
    print(f"{{{strlst}}}")


def main() -> None:
    print_list(PLAYERS)
    cap_lst = [player.capitalize() for player in PLAYERS]
    print_list(cap_lst)
    select_caps = [player for player in PLAYERS if player[0].isupper()]
    print_list(select_caps)
    scores: dict[str, int] = {
        player: random.randint(0, 999) for player in PLAYERS}
    strlst = str()
    for player, score in scores.items():
        strlst += f"{player}: {score}, "
    strlst = strlst[:-2]
    print(f"{{{strlst}}}")
    print(f"Score average is: {round(sum(scores.values()) / len(scores), 2)}")
    top_5 = sorted(scores.items(), key=lambda item: item[1], reverse=True)[:5]
    print_scores(top_5)


if __name__ == "__main__":
    main()
