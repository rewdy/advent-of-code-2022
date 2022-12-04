from art import tprint
from advent_of_code_2022.day_4.data import data


def get_ranges(dashed: str):
    """
    Given a string in the format of `12-15`, return a list representing
    those numbers inclusively.
    """
    first, second = dashed.split("-")
    return list(range(int(first), int(second) + 1))


def process_data():
    """Pull in the puzzle data; split into rows; make into lists of ints."""
    in_rows = [row.split(",") for row in data.split("\n")]
    return [[get_ranges(dashed) for dashed in row] for row in in_rows]


def main():
    tprint("Have a kick-ass Kwanza!")
    puzzle_data = process_data()
    puzzle_data_sets = [[set(g) for g in row] for row in puzzle_data]

    # Part 1
    overlapped = 0
    for s1, s2 in puzzle_data_sets:
        if len(s1 - s2) == 0 or len(s2 - s1) == 0:
            overlapped += 1

    print(f"Overlapping completely: {overlapped}")

    # Part 2
    overlap_at_all = 0
    for s1, s2 in puzzle_data_sets:
        if len(s1.intersection(s2)) > 0:
            overlap_at_all += 1

    print(f"Overlapping at all: {overlap_at_all}")


if __name__ == "__main__":
    main()
