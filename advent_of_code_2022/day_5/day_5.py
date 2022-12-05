from art import tprint
from advent_of_code_2022.day_5.data import piles, moves


def get_piles():
    """takes puzzle data for the piles and makes them lists"""
    rows = [row for row in piles.split("\n")]
    # ↕ to ↔
    rotated = [[row[index] for row in rows] for index in range(0, len(rows[0]))]
    # find the good ones
    good = []
    for row in rotated:
        row.reverse()
        if row[0].isnumeric():
            row.pop(0)  # remove col number
            row = [item for item in row if item != " "]  # remove empties
            good.append(row)

    return good


def process_moves():
    moves_list = moves.split("\n")
    processed = []
    for row in moves_list:
        pieces = row.split(" ")
        processed.append(
            {
                "count": int(pieces[1]),
                "from": int(pieces[3]) - 1,  # make these indexes
                "to": int(pieces[5]) - 1,  # make these indexes
            }
        )
    return processed


def split_from_end(items, count):
    """Returns items from the end, remaining items"""
    return items[-1*count:], items[0:-1*count]


def main():
    tprint("Ho Ho Ho!")
    tprint("- Santa Claus", font="cursive")
    piles_1 = get_piles()
    moves = process_moves()
    # Part 1
    for move in moves:
        for _ in range(move["count"]):
            crate = piles_1[move["from"]].pop()
            piles_1[move["to"]].append(crate)

    on_top = "".join([pile[-1] for pile in piles_1])
    print(f"Part 1: The top crate on each pile is: {on_top}")

    # Part 2
    piles_2 = get_piles()
    for move in moves:
        crates_to_move, remaining_in_stack = split_from_end(piles_2[move["from"]], move["count"])
        piles_2[move["from"]] = remaining_in_stack
        piles_2[move["to"]].extend(crates_to_move)

    on_top_2 = "".join([pile[-1] for pile in piles_2])
    print(f"Part 1: The top crate on each pile is: {on_top_2}")


if __name__ == "__main__":
    main()
