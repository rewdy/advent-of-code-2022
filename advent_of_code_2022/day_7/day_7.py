from art import tprint
from functools import reduce
from advent_of_code_2022.day_7.data import data, test_data
from advent_of_code_2022.utils import save_json
from re import match

FILE_BASE = "./advent_of_code_2022/day_7"
TOTAL_KEY = "_total"
DISK_SIZE = 70000000
SIZE_FOR_UPDATE = 30000000


def dict_path(dict, list):
    """function to pass in a list of keys, and this will return the nested place in a dict"""
    place = dict
    for key in list:
        place = place.get(key)
    return place


def data_to_listing(raw_data):
    dirs_to_process = raw_data.split("\n")
    # keys are dirs
    # children files are under `files`
    # we'll add sizes in a second pass
    tree = {}
    place = []
    for command in dirs_to_process:
        tree_context = dict_path(tree, place)
        # What do we do
        if command.startswith("$ cd"):
            dir_name = command.split("cd ")[1]
            if dir_name == "..":
                place.pop()
            else:
                tree_context[dir_name] = {}
                place.append(dir_name)
        elif match("^[0-9]+", command):
            size, file = command.split(" ")
            tree_context["files"] = [*tree_context.get("files", []), {"name": file, "size": int(size)}]
        # We ignore dir* rows b/c we are already capturing the relevant data via the cd commands.
    return tree


def find_inject_sizes(tree):
    """WARNING: this mutates tree"""
    size = 0
    for key in list(tree.keys()):
        if key == "files":
            files_total = reduce(lambda total, file: total + file["size"], tree[key], 0)
            size += files_total
        else:
            combined_total = find_inject_sizes(tree[key])
            size += combined_total

        tree[TOTAL_KEY] = size
    return size


def find_dir_less_than(dir_name, tree, max=100000):
    dirs = []
    combined_size = 0

    for key in list(tree.keys()):
        if key == TOTAL_KEY:
            if tree[key] <= max:
                dirs.append(dir_name)
                combined_size += tree[key]
        elif key != "files":
            found_dirs, size = find_dir_less_than(key, tree[key], max=max)
            dirs.extend(found_dirs)
            combined_size += size

    return dirs, combined_size


def find_dir_more_than(dir_name, tree, threshold):
    dirs = []

    for key in list(tree.keys()):
        if key == TOTAL_KEY:
            dir_size = tree[key]
            if dir_size >= threshold:
                dirs.append((dir_name, dir_size))
        elif key != "files":
            found_dirs = find_dir_more_than(key, tree[key], threshold)
            dirs.extend(found_dirs)

    # sort smallest to largest
    dirs.sort(key=lambda row: row[1])

    return dirs


def main():
    tprint("Joy to the world!", font="basic")

    # Pull in the data and transform to a tree
    # tree = data_to_listing(test_data)  # test file
    tree = data_to_listing(data)
    save_json(f"{FILE_BASE}/day_7_files.json", tree)
    print("-> Tree built")

    total_size = find_inject_sizes(tree)
    save_json(f"{FILE_BASE}/day_7_files_sizes.json", tree)
    print("-> Sizes added")

    # big dirs
    dirs, combined_size = find_dir_less_than("/", tree["/"])
    save_json(f"{FILE_BASE}/day_7_found_dirs.json", dirs)
    print("-> Found dirs less than 100000")
    print(f"Found {len(dirs)} with combined size of {combined_size}")

    print("------- part 2 -------")

    # part 2
    size_available = DISK_SIZE - total_size
    size_needed = SIZE_FOR_UPDATE - size_available
    print(
        f"Total size is {total_size}. The disk size is {DISK_SIZE}, meaning we have {size_available}"
        + f" available. We need {SIZE_FOR_UPDATE}. That means we need to free up {size_needed}"
    )
    all_dirs_over_size = find_dir_more_than("/", tree["/"], size_needed)
    save_json(f"{FILE_BASE}/day_7_part_2", all_dirs_over_size)
    best_candidate = all_dirs_over_size[0]
    print("The one to delete is:")
    print(best_candidate)


if __name__ == "__main__":
    main()
