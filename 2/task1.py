with open("input_data.txt", "r") as f:
    data = f.read()

lines = data.split("\n")
oppenent_moves = []
my_moves = []
for line in lines:
    line = line.split(" ")
    oppenent_moves.append(line[0])
    my_moves.append(line[1])

selections_scoring = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

win_mapping = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}
draw_mapping = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

total_score = 0
for i in range(len(oppenent_moves)):
    round_score = 0
    if win_mapping[oppenent_moves[i]] == my_moves[i]:
        round_score += 6
    elif draw_mapping[oppenent_moves[i]] == my_moves[i]:
        round_score += 3
    round_score += selections_scoring[my_moves[i]]
    total_score += round_score

print("Total score is: {}".format(total_score))