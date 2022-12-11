import math

with open("input_data.txt", "r") as f:
    data = f.read()

head_moves = data.split("\n")
moves = []

for move in head_moves:
    move = move.split(" ")
    instruction = {"direction": move[0], "amount":int(move[1])}
    moves.append(instruction)

tail_positions = [[0,0]]

def is_adjacent(rope_knot_pos, knot_num):
    knot0 = rope_knot_pos[str(knot_num)]
    knot1 = rope_knot_pos[str(knot_num+1)]
    if abs(knot0[0] - knot1[0]) > 2 and abs(knot0[1] - knot1[1]) > 2:
        assert False, "This should happen, get a grip man"
    elif abs(knot0[0] - knot1[0]) < 2 and abs(knot0[1] - knot1[1]) < 2:
        return True
    else:
        return False

def update_tail_position(tail_positions, rope_knot_pos, knot_num, do_move):
    if knot_num == "8":
        last_tail_position = knottail_positions[-1]
        new_tail_position = [last_tail_position[0] + do_move[0], last_tail_position[1] + do_move[1]]
        tail_positions.append(new_tail_position)
    else:
        rope_knot_pos[str(knot_num)] = [rope_knot_pos[str(knot_num)][0] - do_move[0], rope_knot_pos[str(knot_num)][1] - do_move[1]]
    return tail_positions, rope_knot_pos

def update_rope(rope_knots, knot):
    i0 = str(knot)
    i1 = str(knot+1)
    new_position = [0,0]
    if rope_knots[i0][0] != rope_knots[i1][0] and rope_knots[i0][1] != rope_knots[i1][1]:
        if rope_knots[i0][0] < rope_knots[i1][0]:
            rope_knots[i1][0] -= 1
        elif rope_knots[i0][0] > rope_knots[i1][0]:
            rope_knots[i1][0] += 1
        
        if rope_knots[i0][1] < rope_knots[i1][1]:
            rope_knots[i1][1] -= 1
        elif rope_knots[i0][1] > rope_knots[i1][1]:
            rope_knots[i1][1] += 1
    elif rope_knots[i0][0] - rope_knots[i1][0] > 0:
        rope_knots[i1][0] += 1
    elif rope_knots[i0][0] - rope_knots[i1][0] < 0:
        rope_knots[i1][0] -= 1
    elif rope_knots[i0][1] - rope_knots[i1][1] > 0:
        rope_knots[i1][1] += 1
    elif rope_knots[i0][1] - rope_knots[i1][1] < 0:
        rope_knots[i1][1] -= 1
    if i1 == "9":
        tail_positions.append([rope_knots[i1][0], rope_knots[i1][1]])
    return rope_knots

rope_knot_pos = {"0": [0,0], "1": [0,0], "2":[0,0], "3":[0,0], "4":[0,0], "5":[0,0], "6":[0,0], "7":[0,0], "8":[0,0], "9":[0,0]}
new_tail_position = [0,0]
for move in moves:
    for times in range(int(move["amount"])):
        for i in range(9):
            #move head
            move_tail = [0,0]
            if i == 0:
                t_head_pos = rope_knot_pos[str(i)]
                if move["direction"] == "R":
                    t_head_pos = [t_head_pos[0]+1, t_head_pos[1]]
                elif move["direction"] == "L":
                    t_head_pos = [t_head_pos[0]-1, t_head_pos[1]]
                elif move["direction"] == "U":
                    t_head_pos = [t_head_pos[0], t_head_pos[1]+1]
                elif move["direction"] == "D":
                    t_head_pos = [t_head_pos[0], t_head_pos[1]-1] 
                
                rope_knot_pos[str(i)] = t_head_pos
            if is_adjacent(rope_knot_pos, i):
                break
            else:
                rope_knot_pos = update_rope(rope_knot_pos, i)
            
        
print(len(tail_positions))
unique_tail_positions = []
for pos in tail_positions:
    if pos not in unique_tail_positions:
        unique_tail_positions.append(pos)
print(len(unique_tail_positions))