import json


def save_json(filename, data_to_save):
    """stupid little helper function to save a dict as json file"""
    if not filename.endswith(".json"):
        filename = filename + ".json"
    with open(filename, "w+") as file:
        json.dump(data_to_save, file, indent=2)
    print(f"Saved data to {filename}")