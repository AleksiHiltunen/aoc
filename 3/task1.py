with open("input_data.txt", "r") as f:
    data = f.read()

total_points = 0
lines = data.split("\n")
for line in lines:
    separator = int(len(line)/2)
    first_half = line[:separator]
    end_half = line[separator:]
    for char in first_half:
        if char in end_half:
            if char.islower():
                print(char, ord(char) - 96)
                total_points += ord(char) - 96
            elif char.isupper():
                print(char, ord(char) - 38)
                total_points += ord(char) - 38
            break

print(total_points)