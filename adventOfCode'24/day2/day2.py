from utils import read_input

input = read_input("adventOfCode'24/day2")

small_list = """3 7 4 6 6
74 72 75 73 77
74 73 71 68 67 64 61 60
88 87 84 81 80 79 78
51 52 53 56 59 62
26 25 24 23 20 18 17
45 47 48 51 54 55 58 60"""

def ifSafe(report):
    isSafe = True
    direction = ""
    for ind, level in enumerate(report):
        if ind == len(report) - 1:
            continue
        elif ind == 0:
            if level == report[ind + 1]:
                isSafe = False
                break
            direction = "decrease" if level > report[ind + 1] else "increase"
        elif direction == "increase":
            if level >= report[ind + 1] or (report[ind + 1] - level) > 3:
                isSafe = False
                break
        elif direction == "decrease":
            if level <= report[ind + 1] or (level - report[ind + 1]) > 3:
                isSafe = False
                break
    #print(report, isSafe)
    return isSafe

def getSafeReports(reports_string):
    safeCount = 0
    reports_array = reports_string.split("\n")
    for report in reports_array:
        safeCount = safeCount + 1 if ifSafe(list(map(int, report.split(" ")))) else safeCount
    return safeCount


print(getSafeReports(input))
            
