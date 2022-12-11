with open("input_data.txt", "r") as f:
    data=f.read()

cycle_check = 20
check_interval = 40

cmds = data.split("\n")
register_value = 1

result_sim = 0
cycle = 0
for command in cmds:
    command = command.split(" ")
    if command[0] == "noop":
        cycle += 1
        if cycle == cycle_check:
            print("Signal strengh = {} * {} = {}".format(cycle, register_value, cycle*register_value))
            result_sim += cycle*register_value
            cycle_check += check_interval
    elif command[0] == "addx":
        for i in range(2):
            cycle += 1
            if cycle == cycle_check:
                print("Signal strengh = {} * {} = {}".format(cycle, register_value, cycle*register_value))
                result_sim += cycle*register_value
                cycle_check += check_interval
        register_value += int(command[1])
        
print(result_sim)