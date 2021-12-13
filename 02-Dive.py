### moving_str = input file in gigantic multiline string
movings_list = moving_str.split("\n")

## What do you get if you multiply your final horizontal position by your final depth?
depth = 0
horizontal = 0
for move in movings_list[0:-1]:
    splitted = move.split(" ")
    moving_type = splitted[0]
    moving_size = int(splitted[1])
    if moving_type == "forward":
        horizontal += moving_size
    elif moving_type == "down":
        depth += moving_size
    elif moving_type == "up":
        depth -= moving_size
print(depth * horizontal)


## What do you get if you multiply your final horizontal position by your final depth?
aim = 0
depth = 0
horizontal = 0
for move in movings_list[0:-1]:
    splitted = move.split(" ")
    moving_type = splitted[0]
    moving_size = int(splitted[1])
    if moving_type == "forward":
        horizontal += moving_size
        depth += aim * moving_size
    elif moving_type == "down":
        aim += moving_size
    elif moving_type == "up":
        aim -= moving_size
print(depth * horizontal)