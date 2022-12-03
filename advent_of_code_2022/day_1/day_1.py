from art import text2art
from advent_of_code_2022.day_1.data import data


def get_max():
    data_as_list = data.split("\n")
    list_of_lists = []
    index = 0
    for line in data_as_list:
        if line == "":
            # empty row, new elf
            index += 1
            continue
        if len(list_of_lists) < index + 1:
            list_of_lists.append([int(line)])
        else:
            list_of_lists[index] = [*list_of_lists[index], int(line)]

    max_calories = max([sum(items) for items in list_of_lists])
    return max_calories


def main():
    print(text2art("🎄 Merry Christmas!"))
    print("---")
    print("Day 1 of Advent of Code")

    max_calories = get_max()

    print("That li'l fella is carrying calories adding up to:")
    print(text2art(f"{max_calories}"))
    print(f"{max_calories} 🎅")


if __name__ == "__main__":
    main()
