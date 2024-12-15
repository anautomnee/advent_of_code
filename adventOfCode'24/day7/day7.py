from utils import read_input

input = read_input("adventOfCode'24/day7")

small_input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

def calculate(numbers, operators, res):
    iteration_sum = 0
    for i in range(len(numbers) - 1):
        iteration_sum += (numbers[i] * numbers[i+1]) if operators[i] == '*' else ( numbers[i] + numbers[i+1])
    print(iteration_sum)
    return iteration_sum

def get_calibration(string):
    calibrations = string.split("\n")
    correct_row_values = []
    for row in calibrations:
        row = row.split(": ")
        res = int(row[0])
        numbers = list(map(int, row[1].split(" ")))
        operators = ["*"] * (len(numbers)-1)
        print('res - ', res, 'numbers - ', numbers, 'operators - ', operators)

        # Go through operators
        iteration_sum = 0
        k = len(operators) - 1
        while k >= 0:
                
            if len(operators) > 1:
                iteration_sum = calculate(numbers, operators, res)
            else:
                iteration_sum = (numbers[0] * numbers[1]) if operators[0] == '*' else (numbers[0] + numbers[1])
            if iteration_sum == res:
                correct_row_values.append(row)
            
            k -= 1
    print(correct_row_values)
    return correct_row_values
        
        
        

get_calibration(small_input)