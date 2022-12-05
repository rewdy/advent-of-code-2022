from art import text2art
from pprint import pprint
from advent_of_code_2022.day_1.data import data


def process_data():
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

    return list_of_lists


def get_max(list_of_lists):
    # Part 1
    max_calories = max([sum(items) for items in list_of_lists])
    return max_calories


def get_max_top_three(list_of_lists):
    # Part 2
    summed_sorted = [sum(items) for items in list_of_lists]
    summed_sorted.sort()
    summed_sorted.reverse()
    return sum(summed_sorted[:3])


def main():
    print(text2art("🎄 Merry Christmas!"))
    print("---")
    print("Day 1 of Advent of Code")

    data_processed = process_data()
    max_calories_top_elf = get_max(data_processed)

    print(f"Part 1: The elf carrying the most calories is carrying {max_calories_top_elf} kcal 🎅")

    max_calories_top_three = get_max_top_three(data_processed)
    print(f"Part 2: The three elves carrying the most calories are carrying {max_calories_top_three} kcal 🎅")


if __name__ == "__main__":
    main()
