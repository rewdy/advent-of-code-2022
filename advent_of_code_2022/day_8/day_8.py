from advent_of_code_2022.day_8.data import data as puzzle_data, example_data

SPACER = " "


def prepare_data(data_str):
    """this returns a 2 dimensional array"""
    return [[*row] for row in data_str.split("\n")]


def get_visible_from_outside(data, show_map=False):
    """part 1"""
    matrix = prepare_data(data)
    last_x_index = len(matrix) - 1
    last_y_index = len(matrix[0]) - 1

    visible = set()
    for y, row in enumerate(matrix):
        for x, me in enumerate(row):
            # if we're on an edge, it's visible
            if x in [0, last_x_index] or y in [0, last_y_index]:
                visible.add((x, y))
                if show_map:
                    print("🟩", end=SPACER)
            else:
                # Work our way out in each direction
                north_covers = bool([matrix[ny][x] for ny in range(0, y) if matrix[ny][x] >= me])
                south_covers = bool([matrix[sy][x] for sy in range(y + 1, last_y_index + 1) if matrix[sy][x] >= me])
                west_covers = bool([matrix[y][wx] for wx in range(0, x) if matrix[y][wx] >= me])
                east_covers = bool([matrix[y][ex] for ex in range(x + 1, last_x_index + 1) if matrix[y][ex] >= me])
                if False in [north_covers, south_covers, west_covers, east_covers]:
                    visible.add((x, y))
                    if show_map:
                        print("🟩", end=SPACER)
                else:
                    if show_map:
                        print("⬛️", end=SPACER)
        if show_map:
            print()

    return visible


def find_highest_visibility_score(data):
    """part 2"""
    matrix = prepare_data(data)
    last_x_index = len(matrix) - 1
    last_y_index = len(matrix[0]) - 1

    def lower_list_count(trees, max, reverse=False):
        if reverse:
            trees = list(reversed(trees))
        found = []
        for tree in trees:
            found.append(tree)
            if tree >= max:
                break
        return len(found)

    scores = []
    for y, row in enumerate(matrix):
        for x, me in enumerate(row):
            # Work our way out in each direction
            north_covers = lower_list_count([matrix[ny][x] for ny in range(0, y)], me, True)
            south_covers = lower_list_count([matrix[sy][x] for sy in range(y + 1, last_y_index + 1)], me)
            west_covers = lower_list_count([matrix[y][wx] for wx in range(0, x)], me, True)
            east_covers = lower_list_count([matrix[y][ex] for ex in range(x + 1, last_x_index + 1)], me)
            scores.append(north_covers * south_covers * west_covers * east_covers)

    top_score = sorted(scores, reverse=True)[0]

    return top_score


def main():
    show_maps = False
    test_data = puzzle_data
    visible = get_visible_from_outside(test_data, show_map=show_maps)
    print(f"Visible count: {len(visible)}")

    # part 2
    highest_score = find_highest_visibility_score(test_data)
    print(f"The highest visibility score is: {highest_score}")


if __name__ == "__main__":
    main()
