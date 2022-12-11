from art import tprint
from pprint import pprint
from advent_of_code_2022.day_10.data import puzzle_data, example_data, micro_example_data
from advent_of_code_2022.utils import print_matrix

SCREEN_WIDTH = 40
SCREEN_HEIGHT = 6
OFF = "⬛️"
ON = "💙"


def process_data(data):
    return [None if "noop" in line else int(line.split(" ")[1]) for line in data.split("\n")]


def process_commands(command_list):
    cycle = 0
    register = 1
    log = {}

    def do_log():
        log[cycle] = register

    for c in command_list:
        # first step is always bump the cycle and log
        cycle += 1
        do_log()
        if c is not None:
            cycle += 1
            do_log()
            register += c

    return register, log


def get_strength_at_cycle(cycle_log, indexes):
    return {index: cycle_log[index] * index for index in indexes}


def draw_screen(cycle_log):
    rows = [[OFF for _ in range(SCREEN_WIDTH)] for _ in range(SCREEN_HEIGHT)]  # pre-build our rows
    for cycle, register in cycle_log.items():
        col_index = (cycle - 1) % SCREEN_WIDTH
        row_index = cycle // SCREEN_WIDTH
        sprite_range = [register - 1, register, register + 1]
        if col_index in sprite_range:
            rows[row_index][col_index] = ON
    return rows


def main():
    tprint("Ding dong merely on high")
    print("🥬")

    # commands = process_data(micro_example_data)
    # commands = process_data(example_data)
    commands = process_data(puzzle_data)

    register, cycle_log = process_commands(commands)

    print(f"Register value ends at {register}")
    print()

    indexes_to_check = list(range(20, 221, 40))
    print(f"checking indexes: {indexes_to_check}")
    output = get_strength_at_cycle(cycle_log, indexes_to_check)

    pprint(output)
    print()

    signal_strength_sum = sum(output.values())
    print(f"The sum of the signal strengths is: {signal_strength_sum}")
    print()

    screen = draw_screen(cycle_log)
    print_matrix(screen)


if __name__ == "__main__":
    main()
