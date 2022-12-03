from art import tprint
from advent_of_code_2022.day_3.data import data

ALL_OPTIONS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def score_item(item):
    return ALL_OPTIONS.index(item) + 1


def score_and_sum(list):
    points = [score_item(item) for item in list]
    return sum(points)


def main():
    tprint("Happy Holidays! 🎅", font="script")
    # part 1
    # Our pack contents as a list of tuples
    data_as_list = [
        (row[slice(int(len(row) / 2))], row[slice(int(len(row) / 2), len(row))]) for row in data.split("\n")
    ]
    # Find the item in both
    in_both_sacks = [list(set(r[0]).intersection(set(r[1])))[0] for r in data_as_list]
    # score and sum
    total = score_and_sum(in_both_sacks)
    print(f"Total of all priorities: {total}")

    # part 2, find badges
    as_rows = data.split("\n")
    groups = [as_rows[i:i + 3] for i in range(0, len(as_rows), 3)]
    badges = []
    for group in groups:
        # probably a more efficient way to do this, but...
        common1 = set(group[0]).intersection(set(group[1]))
        common2 = set(group[1]).intersection(set(group[2]))
        final = common1.intersection(common2)
        if final:
            badges.append(list(final)[0])
    total_points_badges = score_and_sum(badges)

    print(f"All badges scored and totalled: {total_points_badges}")


if __name__ == "__main__":
    main()
