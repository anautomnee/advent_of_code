#from utils import read_input

#input = read_input("adventOfCode'24/day6")

small_input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

positions_array = []

def movement_logic(position, direction, map):
    # base case
    print(direction, position)
    if (direction == ">" and position[1] == 0) or (direction == "v" and position[0] == len(map[position[1]]) - 1) or (direction == "<" and position[1] == len(map) - 1) or (direction == "^" and position[0] == 0):
        return 
    
    if direction == "^":
        i = 1
        while map[position[1] - i][position[0]] != "#":
            print(position[1] - i, position[0])
            positions_array.append([position[0], position[1] - i])
            if position[1] - i == 0:
                i += 1
                break
            i += 1
        
        direction = ">"
        movement_logic([position[0], position[1] - i + 1], direction, map)
        return
    if direction == ">":
        i = 1
        while map[position[1]][position[0] + i] != "#":
            print(position[1], position[0] + i)
            positions_array.append([position[0] + i, position[1]])
            if position[0] + i == len(map[position[1]]) - 1:
                i += 1
                break
            i += 1
        direction = "v"
        print([position[0] + i - 1, position[1]])
        movement_logic([position[0] + i - 1, position[1]], direction, map)
        return
    if direction == "v":
        i = 1
        while map[position[1] + i][position[0]] != "#":
            print(position[1] + i, position[0])
            positions_array.append([position[0], position[1] + i])
            if position[1] + i == len(map) - 1:
                i += 1
                break
            i += 1
        direction = "<"
        print([position[0], position[1] + i - 1])
        movement_logic([position[0], position[1] + i - 1], direction, map)
        return 
    if direction == "<":
        i = 1
        while map[position[1]][position[0] - i] != "#":
            print(position[1], position[0] - i)
            positions_array.append([position[0] - i, position[1]])
            if position[0] - i == 0:
                i += 1
                break
            i += 1
        direction = "^"
        print([position[0] - i + 1, position[1]])
        movement_logic([position[0] - i + 1, position[1]], direction, map)
        return
    return     


def log_path(map_string):
    guard_position = [0,0]
    direction = "^"
    map = map_string.split("\n")
    for row in map:
        row.split()

    # Find guard's starting position
    for y, i in enumerate(map):
        for x, j in enumerate(i):
            if j == direction:
                guard_position = [x, y]
    print(guard_position)

    # Movement logic
    positions_array.append(guard_position)
    movement_logic(guard_position, direction, map)
    
    print(positions_array)
    duplicates = 0
    for ind, position in enumerate(positions_array):
        for i in range(ind + 1, len(positions_array)):
            if position == positions_array[i]:
                duplicates += 1
    print(len(positions_array) - duplicates)

log_path(small_input)