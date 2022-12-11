with open("input_data.txt", "r") as f:
    data = f.read()

terminal = data.split("\n")
folder_tree = {"/":[]}
current_directory = "/"

for line in terminal:
    if "$" == line[:1]:
        if line[2:4] == "cd":
            if line[5:7] == "..":
                dirs = current_directory.split("/")
                dirs = dirs[:-2]
                dirs.remove("")
                current_directory = "/".join(dirs)
                if len(current_directory) == 0:
                    current_directory = "/"
                else:
                    current_directory = "/{}/".format(current_directory)
            elif not line[5:] == "/":
                current_directory += line[5:] + "/"

        elif line[2:4] == "ls":
            pass
    else:
        if line[:3] == "dir":
            directory = "{}{}/".format(current_directory, line[4:])
            try:
                _i = folder_tree[directory]
            except:
                folder_tree[directory] = []
        else:
            line = line.split(" ")
            new_file = {"name": line[1], "size": line[0]}
            folder_tree[current_directory].append(new_file)

over_sized_total = 0
for directory in folder_tree:
    directory_size = 0
    for folder_name in folder_tree:
        if directory in folder_name:
            for item in folder_tree[folder_name]:

                directory_size += int(item["size"])
    
    # curr_dir_items = folder_tree[directory]
    # for item in curr_dir_items:
    #     directory_size += int(item["size"])

    print("{} - {}".format(directory, directory_size))
    if directory_size < 100000:
        over_sized_total += directory_size

print("RESULT: {}".format(over_sized_total))
