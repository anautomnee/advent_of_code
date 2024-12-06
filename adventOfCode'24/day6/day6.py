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

class InfiniteLoopException(Exception):
    pass

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

    MAX_ITERATIONS = 10000
    position_loop_counter = 0

    while True:
        try:
            position_loop_counter += 1
            if(position_loop_counter > MAX_ITERATIONS):
                raise InfiniteLoopException("Potential infinite loop detected!")

            dy, dx = directions[direction]
            nx, ny = position[0] + dx, position[1] + dy

            if nx >= len(map[0]) or nx < 0 or ny >= len(map) or ny < 0:
                break

            if map[ny][nx] == '#':
                direction = turnRight[direction]
                continue

            position = [nx, ny]
            positions_array.add(tuple(position))
        except Exception:
            return True
    return False
  


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
    loop_counter = 0
    positions_array = set()
    positions_array.add(tuple(guard_position))

    # Set up obstruction
    for i, row in enumerate(map):
        for j, col in enumerate(row):
            if col != guard_position and col != '#' and col != '^':
                new_arr = list(map[i])
                new_arr[j] = '#'
                map[i] = new_arr
                res = movement_logic(guard_position, direction, map, positions_array)
                # if res:
                #     for row in map:
                #         print(row, "\n")
                #     print("-----------")
                if res:
                    loop_counter += 1
                map[i][j] = '.'
                map[i] = "".join(map[i])

    print(loop_counter)

    #movement_logic(guard_position, direction, map, positions_array, loop_counter)

    #print(len(positions_array))

log_path(input)