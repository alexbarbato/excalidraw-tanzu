import json
import sys

joined_lib = {}

if len(sys.argv) == 1:
    print("No command line arguments passed in. Should specify a series of file headers - e.g. users abc def")

else:
    for (index, arg) in enumerate(sys.argv[1:]):
        file_name = './raw/' + arg + '.excalidrawlib'
        print("Loading file: " + file_name)
        
        f = open(file_name)
        loaded_data = json.load(f)

        if index == 0: 
            joined_lib = loaded_data
        else:
            joined_lib["library"] += loaded_data["library"]

        f.close()

    new_file = open("lib.excalidrawlib", "w")
    new_file.write(json.dumps(joined_lib))
    new_file.close()