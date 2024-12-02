from utils import read_input
import copy

input = read_input("adventOfCode'24/day2")

small_list = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

def ifSafe(report, isModified = False):
    direction = ""
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        
        if i == 0:  # Determine the direction at the start
            if diff == 0:
                return False  # Equal levels are always unsafe
            direction = "increase" if diff > 0 else "decrease"

        # Check if the current pair violates safety rules
        if direction == "increase" and (diff <= 0 or diff > 3):
            return False
        if direction == "decrease" and (diff >= 0 or abs(diff) > 3):
            return False

    return True

def getSafeReports(reports_string):
    safeCount = 0
    reports_array = reports_string.split("\n")
    for report in reports_array:
        levels = list(map(int, report.split(" ")))
        safeCount = safeCount + 1 if ifSafe(levels) or problem_parser(levels) else safeCount
    return safeCount

def problem_parser(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if ifSafe(modified_report, True):
            return True
    return False 

print(getSafeReports(input))
            
