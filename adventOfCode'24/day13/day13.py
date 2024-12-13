from utils import read_input
import re
from sympy import symbols, Eq, solve, Integer

input = read_input("adventOfCode'24/day13")

small_input = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""

#MAX_BTN_PRESS = 100
CORRECTION = 10000000000000

def get_pushes(arr_x, x_result, arr_y, y_result):
    m,n = symbols('m n')
    eq1 = Eq(int(arr_x[0])*m + int(arr_x[1])*n, int(x_result) + CORRECTION)
    eq2 = Eq(int(arr_y[0])*m + int(arr_y[1])*n, int(y_result) + CORRECTION)

    solution = solve((eq1, eq2), (m, n))
    if isinstance(solution[m], Integer) and isinstance(solution[n], Integer):

        return solution[m]*3 + solution[n]
    else: 
        return False

def count_prizes(input_string):
    machines = input_string.split('\n\n')
    count = 0
    for machine in machines:
        x = re.findall('X\\+(\\d+)', machine)
        x_result = re.findall('X=(\\d+)', machine)[0]
        y = re.findall('Y\\+(\\d+)', machine)
        y_result = re.findall('Y=(\\d+)', machine)[0]
        result = get_pushes(x, x_result, y, y_result)
        if result: count+= result
    return count
        
   
result = count_prizes(input)
print(result)


