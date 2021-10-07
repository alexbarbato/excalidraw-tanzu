import glob
import json
import sys

joined_lib = {}
files = []

if len(sys.argv) == 1:
    print("No command line arguments passed in. Will compile all libraries.")
    files = glob.glob("./raw/*")
else:
    for file in sys.argv[1:]:
        files.append('./raw/' + file + '.excalidrawlib')

for (index, file) in enumerate(files):
    print("Loading file: " + file)
    
    with open(file) as f:
        loaded_data = json.load(f)

        if index == 0: 
            joined_lib = loaded_data
        else:
            joined_lib["library"] += loaded_data["library"]

with open("lib.excalidrawlib", "w") as new_file:
    new_file.write(json.dumps(joined_lib))