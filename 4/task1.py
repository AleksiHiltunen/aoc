with open("input_data.txt", "r") as f:
    data = f.read()

lines = data.split("\n")
left = []
right = []
for line in lines:
    line = line.split(",")
    left.append(line[0])
    right.append(line[1])

i = 0
result_pairs = 0
while i < len(left):
    left_item = left[i].split("-")
    right_item = right[i].split("-")
    left_small = int(left_item[0])
    left_big = int(left_item[1])
    right_small = int(right_item[0])
    right_big = int(right_item[1])

    if left_small in range(right_small, right_big+1) and left_big in range(right_small, right_big+1):
        print("Left in range of right")
        result_pairs += 1
    elif right_small in range(left_small, left_big+1) and right_big in range(left_small, left_big+1):
        print("Right in range of left")
        result_pairs += 1
    i += 1
print(result_pairs)