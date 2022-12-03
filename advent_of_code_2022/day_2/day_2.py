from pprint import pprint
from art import tprint
from advent_of_code_2022.day_2.data import data_as_tuples


"""
NOTES:

OPPONENT
---
A: Rock
B: Paper
C: Scissors

YOU
---
X: Rock
Y: Paper
Z: Scissors

Points per shape
---
Rock: 1
Paper: 2
Scissors: 3

Points per outcome
---
Win: 6
Draw: 3
Lose: 0

PART 2

X: lose
Y: draw
Z: win
"""

# part 1
WIN_MAP = {"A": "Y", "B": "Z", "C": "X"}
DRAW_MAP = {"A": "X", "B": "Y", "C": "Z"}

# part 2
WIN_MAP_2 = {"A": "B", "B": "C", "C": "A"}
DRAW_MAP_2 = {"A": "A", "B": "B", "C": "C"}
LOSE_MAP_2 = {"A": "C", "B": "A", "C": "B"}
OUTCOME_TO_MAP = {
    "X": LOSE_MAP_2,
    "Y": DRAW_MAP_2,
    "Z": WIN_MAP_2,
}

POINT_PLAY_TYPE_MAP = {
    # Keep these for part 1 scoring
    "X": 1,
    "Y": 2,
    "Z": 3,
    # These are for part 2 scoring
    "A": 1,
    "B": 2,
    "C": 3,
}


def score_round_part_1(opponent, you):
    """Function to score a round for part 1"""
    my_points = 0
    # did I win?
    if WIN_MAP[opponent] == you:
        my_points += 6
    elif DRAW_MAP[opponent] == you:
        my_points += 3
    # else, you lose
    my_points += POINT_PLAY_TYPE_MAP[you]

    return my_points


def score_round_part_2(opponent, your_outcome):
    """Function to score a round for part 2"""
    play_map = OUTCOME_TO_MAP[your_outcome]
    you = play_map[opponent]
    my_points = 0
    # did I win?
    if WIN_MAP_2[opponent] == you:
        my_points += 6
    elif DRAW_MAP_2[opponent] == you:
        my_points += 3
    # else, you lose
    my_points += POINT_PLAY_TYPE_MAP[you]

    return my_points


def main():
    tprint("🎄 Merry Christmas!!")
    tprint("Day 2, bitches!", font="script")
    all_rounds_points = [score_round_part_1(*round) for round in data_as_tuples]
    total = sum(all_rounds_points)

    print(f"For part 1, total score should be: {total}")

    all_rounds_points_2 = [score_round_part_2(*round) for round in data_as_tuples]
    total_2 = sum(all_rounds_points_2)

    print(f"For part 2, total score should be: {total_2}")


if __name__ == "__main__":
    main()
