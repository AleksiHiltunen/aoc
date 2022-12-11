with open("input_data.txt", "r") as f:
    data = f.read()

head_moves = data.split("\n")
moves = []

for move in head_moves:
    move = move.split(" ")
    instruction = {"direction": move[0], "amount":int(move[1])}
    moves.append(instruction)

tail_positions = [[0,0]]

def is_adjacent(coords):
    if abs(coords[0]) > 2 or abs(coords[1]) > 2:
        assert False, "This should happen, get a grip man"
        
    elif abs(coords[0]) < 2 and abs(coords[1]) < 2:
        return True
    else:
        return False

def update_tail_position(tail_positions, do_move):
    last_tail_position = tail_positions[-1]
    new_tail_position = [last_tail_position[0] + do_move[0], last_tail_position[1] + do_move[1]]
    tail_positions.append(new_tail_position)
    return tail_positions

t_head_pos = [0,0]
new_tail_position = [0,0]
for move in moves:
    for times in range(int(move["amount"])):
        print("moving {} times {}".format(move["direction"], times))
        #move head
        if move["direction"] == "R":
            t_head_pos = [t_head_pos[0]+1, t_head_pos[1]]
        elif move["direction"] == "L":
            t_head_pos = [t_head_pos[0]-1, t_head_pos[1]]
        elif move["direction"] == "U":
            t_head_pos = [t_head_pos[0], t_head_pos[1]+1]
        elif move["direction"] == "D":
            t_head_pos = [t_head_pos[0], t_head_pos[1]-1]

        if is_adjacent(t_head_pos):
            print("no need to move")
        else:
            #move tail towards head
            move_tail = [0,0]
            if t_head_pos[0] == -2 and t_head_pos[1] == -1:
                move_tail = [-1, -1]
            elif t_head_pos[0] == -2 and t_head_pos[1] == 1:
                move_tail = [-1, +1]
            elif t_head_pos[0] == 2 and t_head_pos[1] == -1:
                move_tail = [1, -1]
            elif t_head_pos[0] == 2 and t_head_pos[1] == 1:
                move_tail = [1, 1]

            elif t_head_pos[1] == -2 and t_head_pos[0] == -1:
                move_tail = [-1, -1]
            elif t_head_pos[1] == -2 and t_head_pos[0] == 1:
                move_tail = [1, -1]
            elif t_head_pos[1] == 2 and t_head_pos[0] == -1:
                move_tail = [-1, 1]
            elif t_head_pos[1] == 2 and t_head_pos[0] == 1:
                move_tail = [1, 1]

            elif t_head_pos[0] == -2:
                move_tail = [-1, 0]
            elif t_head_pos[0] == 2:
                move_tail = [1, 0]
            elif t_head_pos[1] == -2:
                move_tail = [0, -1]
            elif t_head_pos[1] == 2:
                move_tail = [0, 1]
            print("HEAD NEW POSITION: {}".format(str(t_head_pos)))
            print("moving tail {}".format(str(move_tail)))
            tail_positions = update_tail_position(tail_positions, move_tail)
            t_head_pos = [t_head_pos[0] - move_tail[0], t_head_pos[1] - move_tail[1]]
            print("HEAD_RELATIVE_POSITION AFTER TAIL MOVE: {}".format(t_head_pos))
        
print(len(tail_positions))
unique_tail_positions = []
for pos in tail_positions:
    if pos not in unique_tail_positions:
        unique_tail_positions.append(pos)
print(len(unique_tail_positions))