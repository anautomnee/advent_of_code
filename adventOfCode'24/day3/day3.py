import re
from utils import read_input

input = read_input("adventOfCode'24/day3")
small_input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

def get_multiplication_res(string):
    result = 0
    isEnabled = True
    regex_incorrupt = "mul\\([0-9]{1,3},[0-9]{1,3}\\)|don't\\(\\)|do\\(\\)"
    incorrupted = re.findall(regex_incorrupt, string)
    for set in incorrupted:
        if set == "do()":
            isEnabled = True
        elif set == "don't()":
            isEnabled = False
        else:
            if not isEnabled:
                continue
            numbers = re.findall("[0-9]{1,3}", set)
            result += int(numbers[0]) * int(numbers[1])
    return result


result = get_multiplication_res(input)
print(result)
    