from utils import read_input

input = read_input("adventOfCode'24/day4")

small_input = """....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX"""

def findXmas(string):
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

print(findXmas(input))