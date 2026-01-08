# python reading files (.txt, .json, .csv)

file_path = "output.txt"

try:
    with open(file_path, "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
        print("File not found")
except PermissionError:
    print("you dont have permission")