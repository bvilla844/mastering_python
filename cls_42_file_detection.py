# python file detection

import os

file_path = "stuff/test"

if os.path.exists(file_path):
    print(f"the location '{file_path}' exists")

    if os.path.isfile(file_path):
        print(f"that is a file")
    else:
        os.path.isdir(file_path)
        print(f"that is a directory")
else:
    print("that location does not exists")