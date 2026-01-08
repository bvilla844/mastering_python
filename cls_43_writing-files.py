# python writing files (.txt, .json, .csv)
import json

employess = {
    "name": "spongebob",
    "age": 30,
    "job": "cook"
}

file_path = "output.json"

try:
    with open(file_path, "w") as f:
        json.dump(employess, f, indent=4)
        print(f"json file {file_path} was created")
except FileExistsError:
    print(f"text file {file_path} already exists")

