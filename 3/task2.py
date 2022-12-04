with open("input_data.txt", "r") as f:
    data = f.read()

total_points = 0
lines = data.split("\n")
i = 0
while i < len(lines):
    for char in lines[i]:
        if char in lines[i+1] and char in lines[i+2]:
            if char.islower():
                print(char, ord(char) - 96)
                total_points += ord(char) - 96
            elif char.isupper():
                print(char, ord(char) - 38)
                total_points += ord(char) - 38
            i += 3
            break

print(total_points)