with open("input_data.txt", "r") as f:
    data = f.read()

lines = data.split("\n")
oppenent_moves = []
result = []
for line in lines:
    line = line.split(" ")
    oppenent_moves.append(line[0])
    result.append(line[1])

win_selection = {
    "A": "B",
    "B": "C",
    "C": "A"
}

lose_selection = {
    "A": "C",
    "B": "A",
    "C": "B"
}

selections_scoring = {
    "A": 1,
    "B": 2,
    "C": 3
}

total_score = 0
for i in range(len(oppenent_moves)):
    round_score = 0
    if result[i] == "X":
        my_move = lose_selection[oppenent_moves[i]]
    elif result[i] == "Y":
        my_move = oppenent_moves[i]
        round_score += 3
    else:
        my_move = win_selection[oppenent_moves[i]]
        round_score += 6

    round_score += selections_scoring[my_move]
    total_score += round_score

print("Total score is: {}".format(total_score))