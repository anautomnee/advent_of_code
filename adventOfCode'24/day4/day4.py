from utils import read_input

input = read_input("adventOfCode'24/day4")

small_input = """.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
.........."""

# Task 1

def find_xmas(string):
    array = string.split("\n")
    count = 0
    for i, row in enumerate(array):
        for y, el in enumerate(row):
            if el == 'X':
                # right
                if len(row) - 1 - y >= 3 and ''.join([el, row[y + 1], row[y + 2], row[y + 3]]) == 'XMAS':
                    count += 1
                # left
                if y >= 3 and ''.join([el, row[y - 1], row[y - 2], row[y - 3]]) == 'XMAS':
                    count += 1
                # up
                if i >= 3 and ''.join([el, array[i - 1][y], array[i - 2][y], array[i - 3][y]]) == 'XMAS':
                    count += 1
                # down
                if len(array) - 1 - i >= 3 and ''.join([el, array[i + 1][y], array[i + 2][y], array[i + 3][y]]) == 'XMAS':
                    count += 1
                # upright
                if i >= 3 and len(row) - 1 - y >= 3 and ''.join([el, array[i - 1][y + 1], array[i - 2][y + 2], array[i - 3][y + 3]]) == 'XMAS':
                    count += 1
                # upleft
                if i >= 3 and y >= 3 and ''.join([el, array[i - 1][y - 1], array[i - 2][y - 2], array[i - 3][y - 3]]) == 'XMAS':
                    count += 1
                # downright
                if len(array) - 1 - i >= 3 and len(row) - 1 - y >= 3 and ''.join([el, array[i + 1][y + 1], array[i + 2][y + 2], array[i + 3][y + 3]]) == 'XMAS':
                    count += 1
                # downleft
                if len(array) - 1 - i >= 3 and y >= 3 and ''.join([el, array[i + 1][y - 1], array[i + 2][y - 2], array[i + 3][y - 3]]) == 'XMAS':
                    count += 1
    return count

# Task 2

def find_x_mas(string):
    array = string.split("\n")
    count = 0
    for i, row in enumerate(array):
        for y, el in enumerate(row):
            if el == 'A':
                # right diagonal
                if i >= 1 and len(array) - 1 - i >= 1 and len(row) - 1 - y >= 1 and y >= 1:
                    a = ''.join([array[i + 1][y + 1], el, array[i - 1][y - 1]])
                    b = ''.join([array[i + 1][y - 1], el, array[i - 1][y + 1]])
                    if (a == 'MAS' or a == 'SAM') and (b == 'MAS' or b == 'SAM'):
                        count += 1
    return count

print(find_x_mas(input))