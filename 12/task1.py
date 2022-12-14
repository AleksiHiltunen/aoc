import time
import os, sys

with open("test_input.txt", "r") as f:
    data = f.read()


MAX_STEPS = 99999999999
lines = data.split("\n")
e_map = []
visited_map = []
paths = []
for line in lines:
    new_line = []
    visited_line = []
    for char in line:
        new_line.append(char)
        visited_line.append(MAX_STEPS)
    e_map.append(new_line)
    visited_map.append(visited_line)

for i in range(len(e_map)):
    for j in range(len(e_map[i])):
        if e_map[i][j] == "S":
            paths = [[[i,j]]]
            visited_map[i][j] = 1
        elif e_map[i][j] == "E":
            end_x = i
            end_y = j

def print_path(path):
    print_line = ""
    for i in range(41):
        for j in range(160):
            if [i, j] in path:
                char = e_map[i][j]
            else:
                char = "-"
            print_line += str(char)
        print_line +="\n"
    print(print_line, flush=True)
    #time.sleep(0.01)

def print_visited():
    global visited_map
    print_line = ""
    for i in range(len(visited_map)):
        for j in range(len(visited_map[0])):
            if visited_map[i][j] != MAX_STEPS:
                char = "O"
            else:
                char = "-"
            print_line += str(char)
        print_line +="\n"
    print(print_line)

def go_horizontal(path, d_x):
    global visited_map
    current_elevation = e_map[path[-1][0]][path[-1][1]]
    if current_elevation == "S":
        current_elevation = "a"
    if path[-1][0] + d_x < len(e_map) and path[-1][0] + d_x >= 0:
        target = [path[-1][0] + d_x, path[-1][1]]
        new_elevation = e_map[target[0]][target[1]]
        if new_elevation == "E":
            new_elevation = "z"
        if (ord(new_elevation) <= ord(current_elevation)+1):
            if target not in path:
                if visited_map[target[0]][target[1]] > len(path) + 1:
                    visited_map[target[0]][target[1]] = len(path) + 1
                    path = path + [target]
                    return path
    return None

def go_vertical(path, d_y):
    global visited_map
    current_elevation = e_map[path[-1][0]][path[-1][1]]
    if current_elevation == "S":
        current_elevation = "a"
    if path[-1][1] + d_y < len(e_map[0]) and path[-1][1] + d_y >= 0:
        target = [path[-1][0], path[-1][1] + d_y]
        new_elevation = e_map[target[0]][target[1]]
        if new_elevation == "E":
            new_elevation = "z"
        if (ord(new_elevation) <= ord(current_elevation)+1):
            if target not in path:
                if visited_map[target[0]][target[1]] > len(path) + 1:
                    visited_map[target[0]][target[1]] = len(path) + 1
                    path = path + [target]
                    return path
    return None

def is_map_done():
    global end_x, end_y, visited_map
    if visited_map[end_x][end_y] != MAX_STEPS:
        return True
    return False    

path_length = 1
while True:
    if is_map_done():
        break
    new_paths = []
    for path in paths:
        path1 = go_vertical(path, 1)
        if path1:
            new_paths.append(path1)
        path2 = go_horizontal(path, 1)
        if path2:
            new_paths.append(path2)
        path3 = go_vertical(path, -1)
        if path3:
            new_paths.append(path3)
        path4 = go_horizontal(path, -1)
        if path4:
            new_paths.append(path4)
    paths = new_paths
    path_length += 1
        
print(path_length)
# for path in paths:
#     print_path(path)

