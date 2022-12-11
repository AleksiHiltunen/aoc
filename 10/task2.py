with open("input_data.txt", "r") as f:
    data=f.read()

cmds = data.split("\n")
register_value = 1
result_screen = []

cycle = 0
for command in cmds:
    command = command.split(" ")
    if command[0] == "noop":
        if register_value-1 == cycle:
            result_screen.append("#")
        elif register_value == cycle:
            result_screen.append("#")
        elif register_value+1 == cycle:
            result_screen.append("#")
        else:
            result_screen.append(" ")
        cycle += 1
        if cycle == 40:
            cycle = 0
    elif command[0] == "addx":
        for i in range(2):
            if register_value-1 == cycle:
                result_screen.append("#")
            elif register_value == cycle:
                result_screen.append("#")
            elif register_value+1 == cycle:
                result_screen.append("#")
            else:
                result_screen.append(" ")
            cycle += 1
            if cycle == 40:
                cycle = 0
        register_value += int(command[1])
    print(register_value)

print(result_screen)
line_print = [39, 79, 119, 159, 199, 239]  
line = ""
i = 0
while i in range(40*6):
    line += result_screen[i]
    if i in line_print:
        print(line)
        line = ""

    i += 1