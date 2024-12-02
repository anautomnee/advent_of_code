from utils import read_input

list = read_input("adventOfCode'24/day1")

smallList = """3   4
4   3
2   5
1   3
3   9
3   3"""


def separateLists(string):
    array = string.replace("\n", "   ").split("   ")
    arr1 = []
    arr2 = []
    for ind, number in enumerate(array):
        if ind % 2:
            arr2.append(int(number))
        else:
            arr1.append(int(number))
    return arr1, arr2


def getDistance(arr1, arr2):
    distance = 0
    arr1.sort()
    arr2.sort()
    for i in range(len(arr1)):
        distance += abs(arr1[i] - arr2[i])
    return distance

def getSimilarity(arr1, arr2):
    similarity = 0
    for i in range(len(arr1)):
        frequency = 0
        for j in range(len(arr2)):
            if arr2[j] == arr1[i]:
                frequency += 1
        similarity += arr1[i] * frequency
    return similarity
            

list1, list2 = separateLists(list)
distance = getDistance(list1, list2)
similarity = getSimilarity(list1, list2)
print(similarity)