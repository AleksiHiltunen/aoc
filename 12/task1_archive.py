import sys, os
import time

with open("input_data.txt", "r") as f:
    data = f.read()


MAX_STEPS = 99999999999
lines = data.split("\n")
e_map = []
visited_map = []
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
            me["path"] = [[i, j]]
            visited_map[i][j] = 1
        elif e_map[i][j] == "E":
            end_x = i
            end_y = j

def print_path(me):
    os.system("clear")
    print_line = ""
    for i in range(41):
        for j in range(160):
            if [i, j] in me["path"]:
                char = "O"
            else:
                char = "-"
            print_line += str(char)
        print_line +="\n"
    print(print_line, flush=True)
    print(me, flush=True)
    time.sleep(0.1)

def is_map_done(visited_map):
    global end_x, end_y
    if (visited_map[end_x][end_y] != MAX_STEPS and 
        visited_map[end_x-1][end_y] != MAX_STEPS and
        visited_map[end_x+1][end_y] != MAX_STEPS and
        visited_map[end_x][end_y-1] != MAX_STEPS and
        visited_map[end_x][end_y+1] != MAX_STEPS):
        return True
    return False

def go_direction(d_x, d_y):
    global visited_map, e_map, me
    new_x = me["path"][-1][0] + d_x
    new_y = me["path"][-1][1] + d_y
    if new_x < 0 or new_x >= len(e_map) - 1:
        return me, visited_map, False
    if new_y < 0 or new_y >= len(e_map[0]) - 1:
        return me, visited_map, False

    new_position = e_map[new_x][new_y]
    can_go = False
    if (ord(me["elevation"]) == ord(new_position)-1 or
        ord(me["elevation"]) == ord(new_position) or
        ord(me["elevation"]) == ord(new_position)+1):
        new_position_value = visited_map[new_x][new_y]
        if visited_map[me["path"][-1][0]][me["path"][-1][1]] + 1 < new_position_value:
            visited_map[new_x][new_y] = visited_map[me["path"][-1][0]][me["path"][-1][1]] + 1
            me["path"].append([new_x, new_y])
            me["elevation"] = e_map[new_x][new_y]
            print_path(me)
            can_go = True
    return can_go

def do_trekking():
    global visited_map, e_map, me
    try:
        if is_map_done(visited_map):
            return

        can_go_1 = go_direction(1,  0)
        can_go_2 = go_direction(0,  1)
        can_go_3 = go_direction(0, -1)
        can_go_4 = go_direction(1, 0)
        if not can_go_1 and not can_go_2 and not can_go_3 and not can_go_4:
            me["path"] = me["path"][:-1]

    except Exception as e:
        print_path(me)
        print(e)
        sys.exit(1)

    return do_trekking()
do_trekking()

