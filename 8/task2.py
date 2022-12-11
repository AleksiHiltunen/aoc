with open("input_data.txt", "r") as f:
    data = f.read()

data = data.split("\n")

tree_map = []
for line in data:
    row = []
    for char in line:
        row.append(int(char))
    tree_map.append(row)

visible_trees = []
col = 0
max_scenic_value = 0
while col in range(len(tree_map)):
    row = 0
    while row in range(len(tree_map[0])):
        tree_height = tree_map[col][row]
        #look up
        i = row-1
        trees_up = 0
        while i >= 0:
            if tree_height <= tree_map[col][i]:
                trees_up += 1
                break
            elif tree_height > tree_map[col][i]:
                cant_see_smaller = tree_map[col][i]
                trees_up += 1
            i -= 1
        #look left
        j = col-1
        trees_left = 0
        while j >= 0:
            if tree_height <= tree_map[j][row]:
                trees_left += 1
                break
            elif tree_height > tree_map[j][row]:
                cant_see_smaller = tree_map[j][row]
                trees_left += 1
            j -= 1
        #look down
        i = row+1
        trees_down = 0
        while i < len(tree_map[0]):
            if tree_height <= tree_map[col][i]:
                trees_down += 1
                break
            elif tree_height > tree_map[col][i]:
                cant_see_smaller = tree_map[col][i]
                trees_down += 1
            i += 1
        #look right
        j = col+1
        trees_right = 0
        while j < len(tree_map):
            if tree_height <= tree_map[j][row]:
                trees_right += 1
                break
            elif tree_height > tree_map[j][row]:
                cant_see_smaller = tree_map[j][row]
                trees_right += 1
            j += 1

        scenic_value = trees_up * trees_down * trees_left * trees_right
        if scenic_value > max_scenic_value:
            max_scenic_value = scenic_value
            max_col = col
            max_row = row
            max_up = trees_up
            max_left = trees_left
            max_down = trees_down
            max_right = trees_right
            
        row += 1

    col += 1

print(tree_map[max_col][max_row])
print(max_col, max_row)
print("  {}  ".format(max_up))
print("{}  {}".format(max_left, max_right))
print("  {}  ".format(max_down))
print("RESULT")
print(max_scenic_value)


first_line = " "
for j in range(len(tree_map[0])):
    if j != max_row:
        first_line += " "
    else:
        first_line += "|"
    j += 1
print(first_line)
i = 0
while i in range(len(tree_map)):
    if i == max_col:
        print_line = "-"
    else:
        print_line = " "
    line = tree_map[i]
    for char in line:
        print_line += str(char)
    print(print_line)
    i += 1