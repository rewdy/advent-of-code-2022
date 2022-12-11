from pprint import pprint
from advent_of_code_2022.day_9.data import puzzle_data, example_data, example_data2


SPACER = " "

move_map = {
    "U": lambda x, y: (x, y - 1),
    "D": lambda x, y: (x, y + 1),
    "L": lambda x, y: (x - 1, y),
    "R": lambda x, y: (x + 1, y),
}


def up_down_1(num):
    if num > 0:
        return 1
    if num < 0:
        return -1
    return 0


def print_matrix(m):
    """helper function to print 2d list"""
    for row in m:
        for col in row:
            print(col, end=SPACER)
        print()


def process_data(data):
    return [(row.split(" ")[0], int(row.split(" ")[1])) for row in data.split("\n")]


def determine_positions(commands, tail_count=9):
    start = (0, 0)  # arbitrarily, we're calling this 0,0; could be any ints
    head_points = [start]
    tail_points = [[start] for _ in range(tail_count)]
    for direction, steps in commands:
        for _ in range(steps):
            # Move the head
            new_head_loc = move_map[direction](*head_points[-1])
            head_points.append(new_head_loc)

            # Move the tail
            for tail_idx in range(tail_count):
                follow_loc = head_points[-1] if tail_idx == 0 else tail_points[tail_idx - 1][-1]
                new_tail_loc = tail_points[tail_idx][-1]
                x_off, y_off = (follow_loc[0] - new_tail_loc[0], follow_loc[1] - new_tail_loc[1])
                distance = sum([abs(n) for n in [x_off, y_off]])
                # if the distance is 0 or 1, it doesn't need to move
                if distance == 2:
                    new_x = new_tail_loc[0] + up_down_1(x_off) if abs(x_off) > 1 else new_tail_loc[0]
                    new_y = new_tail_loc[1] + up_down_1(y_off) if abs(y_off) > 1 else new_tail_loc[1]
                    new_tail_loc = (new_x, new_y)
                elif distance > 2:
                    new_x = new_tail_loc[0] + up_down_1(x_off)
                    new_y = new_tail_loc[1] + up_down_1(y_off)
                    new_tail_loc = (new_x, new_y)

                tail_points[tail_idx].append(new_tail_loc)

    return head_points, tail_points


def plot(head_points, all_tail_points=[], print_after_each=False, print_head=False, clear_after_each=False):
    """this is unnecessary but I want to see a visual to verify"""
    x_min = min([point[0] for point in head_points])
    x_max = max([point[0] for point in head_points])
    y_min = min([point[1] for point in head_points])
    y_max = max([point[1] for point in head_points])
    row_count = x_max - x_min + 1  # needs to be inclusive
    col_count = y_max - y_min + 1  # needs to be inclusive
    x_offset = 0 - x_min
    y_offset = 0 - y_min
    points_adjusted = [(p[0] + x_offset, p[1] + y_offset) for p in head_points]
    tail_points_adjusted = [
        [(p[0] + x_offset, p[1] + y_offset) for p in tail_points] for tail_points in all_tail_points
    ]
    matrix = [["." for _ in range(row_count)] for _ in range(col_count)]
    if print_head:
        if print_after_each:
            print("== PRINTING HEAD ==")
        for point in points_adjusted:
            x, y = point
            matrix[y][x] = "H"
            if print_after_each:
                print_matrix(matrix)
                print("--")

    if print_after_each:
        print("== PRINTING TAIL ==")
    for point_idx in range(len(tail_points_adjusted[0])):
        if clear_after_each:
            matrix = [["." for _ in range(row_count)] for _ in range(col_count)]
        for tail_idx in range(len(tail_points_adjusted)):
            x, y = tail_points_adjusted[tail_idx][point_idx]
            prev_x, prev_y = tail_points_adjusted[tail_idx - 1][point_idx] if tail_idx > 0 else (None, None)
            if (x, y) != (prev_x, prev_y):
                matrix[y][x] = "T" if len(tail_points_adjusted) == 1 else tail_idx + 1
        if clear_after_each and print_after_each:
            head_x, head_y = points_adjusted[point_idx]
            matrix[head_y][head_x] = "H"
        if print_after_each:
            print_matrix(matrix)
            print("--")

    if not print_after_each:
        print_matrix(matrix)


def main():
    commands = process_data(puzzle_data)
    # commands = process_data(example_data)
    # commands = process_data(example_data2)

    tail_count = 9
    head_stops, tail_stops = determine_positions(commands, tail_count)

    should_print = len(commands) < 100

    if should_print:
        plot(head_stops, tail_stops, print_after_each=should_print, clear_after_each=True)

    unique_tail_positions = len(set(tail_stops[-1]))
    print(f"The last tail was in {unique_tail_positions} positions at least once.")


if __name__ == "__main__":
    main()
