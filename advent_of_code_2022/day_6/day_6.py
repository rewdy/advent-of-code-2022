from art import tprint
from advent_of_code_2022.day_6.data import data


def find_start(data, marker_length=4):
    index = marker_length
    found_at_index = None
    while found_at_index is None:
        start_index = index - marker_length
        chunk = data[start_index:index]
        if len(chunk) == len(set(chunk)):
            print(f"Found it: {chunk}")
            found_at_index = int(index)
        else:
            index += 1
    return index


def main():
    tprint("Merry Xmas", font="script")
    # Part 1
    start_of_packet = find_start(data)
    print(f"- Packet starts at index: {start_of_packet}")

    # Part 2
    start_of_packet = find_start(data, marker_length=14)
    print(f"- Message starts at index: {start_of_packet}")


if __name__ == "__main__":
    main()
