from pprint import pprint
from art import text2art, randart
from yaspin import yaspin
from advent_of_code_2022.day_1.data import data


def get_data():
    data_as_list = data.split("\n")
    by_elf = {}
    index = 0
    for line in data_as_list:
        if line == "":
            index += 1
            continue
        elf_key = index
        values = [
            *by_elf.get(elf_key, {}).get("values", []),
            int(line)
        ]
        total = sum(values)
        by_elf[elf_key] = {
            "values": values,
            "total": total,
        }
    return by_elf


def main():
    print(text2art("🎄 Merry Christmas!"))
    print("---")
    print("Day 1 of Advent of Code")

    with yaspin(text="Processing elf calorie data") as spinner:
        data = get_data()
        spinner.ok()

    with yaspin(text="Finding the elf who carried the most calories") as spinner:
        max_calories = 0
        elf_index = None
        for elf, elf_data in data.items():
            if elf_data["total"] > max_calories:
                max_calories = elf_data["total"]
                elf_index = elf
        print(text2art("Done!"))
        print(f"The elf carrying the most calories is elf number {elf_index + 1}")
        print("That li'l fella is carrying calories adding up to:")
        print(text2art(f"{max_calories}"))
        print(max_calories)


if __name__ == "__main__":
    main()
