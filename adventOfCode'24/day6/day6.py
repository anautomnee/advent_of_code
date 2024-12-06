from utils import read_input

input = read_input("adventOfCode'24/day6")

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


def movement_logic(position, direction, map, positions_array):
    
    directions = {
        "^": (-1, 0),
        ">": (0, 1),
        "v": (1, 0),
        "<": (0, -1)
    }

    turnRight = {
        "^": ">",
        ">": "v",
        "v": "<",
        "<": "^"
    }

    while True:

        dy, dx = directions[direction]
        nx, ny = position[0] + dx, position[1] + dy

        if nx >= len(map[0]) or nx < 0 or ny >= len(map) or ny < 0:
            break

        if map[ny][nx] == '#':
            direction = turnRight[direction]
            continue

        position = [nx, ny]
        positions_array.add(tuple(position))
  


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

    # Movement logic
    positions_array = set()
    positions_array.add(tuple(guard_position))
    movement_logic(guard_position, direction, map, positions_array)

    print(len(positions_array))

log_path(input)