import json


def sort_by_id(file_name):
    with open(file_name) as f:
        data = json.load(f)

    sorted_hadiths = sorted(data["hadith"], key=lambda x: x["id"])

    sorted_data = {"hadith": sorted_hadiths}

    with open(file_name, "w") as f:
        json.dump(sorted_data, f, indent=4)


def remove_duplicate(file_name):
    with open(file_name) as f:
        data = json.load(f)

    unique_data = list({json.dumps(item, sort_keys=True) for item in data["hadith"]})
    unique_data = [json.loads(item) for item in unique_data]

    unique_json = {"hadith": unique_data}

    with open(file_name, "w") as f:
        json.dump(unique_json, f, indent=4)


# remove_duplicate("abudawud.json")
# remove_duplicate("ibnmajah.json")
# remove_duplicate("tirmidhi.json")

# sort_by_id("abudawud.json")
sort_by_id("ibnmajah.json")
# sort_by_id("tirmidhi.json")
