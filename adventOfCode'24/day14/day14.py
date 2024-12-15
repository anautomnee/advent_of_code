from utils import read_input
import math

input = read_input("adventOfCode'24/day14")

small_input = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""

TILES_WIDTH = 101
TILES_HEIGHT = 103
MIDDLE_COLUMN = math.floor(TILES_WIDTH/2)
MIDDLE_ROW = math.floor(TILES_HEIGHT/2)


def create_map():
    map = []
    for i in range(TILES_HEIGHT):
        row = []
        for j in range(TILES_WIDTH):
            row.append(0)
        map.append(row)
    return map


def get_positions_and_velocity(placement_string):
    placement_array = placement_string.split('\n')
    positions = []
    velocity = []
    for line in placement_array:
        space_divided = line.split(' ')
        p_eq_divided = space_divided[0].split('=')
        v_eq_divided = space_divided[1].split('=')
        p_numbers = p_eq_divided[1].split(',')
        v_numbers = v_eq_divided[1].split(',')
        positions.append([int(p_numbers[0]), int(p_numbers[1])])
        velocity.append([int(v_numbers[0]), int(v_numbers[1])])
    return positions, velocity

def place_robots(input):
    map = create_map()
    last_positions = []
    positions, velocity = get_positions_and_velocity(input)
    for i in range(100):
        for j, position in enumerate(positions):
            next_x = position[0] + velocity[j][0]
            next_y = position[1] + velocity[j][1]
            # Check if next step is out of range
            if position[0] + velocity[j][0] > TILES_WIDTH - 1:
                next_x = position[0] + velocity[j][0] - TILES_WIDTH
            elif position[0] + velocity[j][0] < 0:
                next_x = TILES_WIDTH + position[0] + velocity[j][0]

            if position[1] + velocity[j][1] > TILES_HEIGHT - 1:
                next_y = position[1] + velocity[j][1] - TILES_HEIGHT
            elif position[1] + velocity[j][1] < 0:
                next_y = TILES_HEIGHT + position[1] + velocity[j][1]

            positions[j] = [next_x, next_y]
            if i == 99:
                last_positions.append(positions[j])

    for position in last_positions:
        map[int(position[1])][int(position[0])] += 1

    q1, q2, q3, q4 = 0, 0, 0, 0
    for i in range(TILES_HEIGHT):
        for j in range(TILES_WIDTH):
            # quadrant 1
            if i < MIDDLE_ROW and j < MIDDLE_COLUMN:
                q1 += map[i][j]
            # quadrant 2
            if i < MIDDLE_ROW and j > MIDDLE_COLUMN:
                q2 += map[i][j]
            # quadrant 3
            if i > MIDDLE_ROW and j < MIDDLE_COLUMN:
                q3 += map[i][j]
            # quadrant 4
            if i > MIDDLE_ROW and j > MIDDLE_COLUMN:
                q4 += map[i][j]

    return q1 * q2 * q3 * q4



count = place_robots(input)
print(count)