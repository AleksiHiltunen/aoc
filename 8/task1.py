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

while col < len(tree_map):
    row = 0
    highest = tree_map[col][row]
    if [col, row] not in visible_trees:
        visible_trees.append([col, row])
    while row < len(tree_map[0]):
        if highest < tree_map[col][row]:
            highest = tree_map[col][row]
            if [col, row] not in visible_trees:
                visible_trees.append([col, row])
            else: 
                print("This tree is already counted as visible tree")
            if highest == 9:
                break
        row += 1
    col += 1
side_trees = 0
print("looking from left, saw {} trees".format(len(visible_trees)-side_trees))
side_trees = len(visible_trees)

col = 0
while col < len(tree_map):
    row = len(tree_map[col])-1
    highest = tree_map[col][len(tree_map[row])-1]
    if [col, row] not in visible_trees:
        visible_trees.append([col, row])
    while row > 0:
        if highest < tree_map[col][row]:
            highest = tree_map[col][row]
            if [col, row] not in visible_trees:
                visible_trees.append([col, row])
            else: 
                print("This tree is already counted as visible tree")
            if highest == 9:
                break
        row -= 1
    col += 1
print("looking from right, saw {} trees".format(len(visible_trees)-side_trees))
side_trees = len(visible_trees)

row = 0
while row < len(tree_map):
    col = 0
    highest = tree_map[col][row]
    if [col, row] not in visible_trees:
        visible_trees.append([col, row])
    while col < len(tree_map[0]):
        if highest < tree_map[col][row]:
            highest = tree_map[col][row]
            if [col, row] not in visible_trees:
                visible_trees.append([col, row])
            else: 
                print("This tree is already counted as visible tree")
            if highest == 9:
                break
        col += 1
    row += 1    
print("looking from top, saw {} trees".format(len(visible_trees)-side_trees))
side_trees = len(visible_trees)

row = 0
while row < len(tree_map):
    col = len(tree_map)-1
    highest = tree_map[col][row]
    if [col, row] not in visible_trees:
        visible_trees.append([col, row])
    while col >= 0:
        if highest < tree_map[col][row]:
            highest = tree_map[col][row]
            if [col, row] not in visible_trees:
                visible_trees.append([col, row])
            else: 
                print("This tree is already counted as visible tree")
            if highest == 9:
                break
        col -= 1
    row += 1
print("looking from bottom, saw {} trees".format(len(visible_trees)-side_trees))

for tree in visible_trees:
    if tree[0] == 0 or tree[1] == 0 or tree[0] == len(tree_map)-1 or tree[1] == len(tree_map[0])-1:
        print("({},{}) -- {} || Edge tree".format(tree[0], tree[1], tree_map[tree[0]][tree[1]]))
    else:
        print("({},{}) -- {}".format(tree[0], tree[1], tree_map[tree[0]][tree[1]]))
print(len(visible_trees))
