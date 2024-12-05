from utils import read_input
import math

input = read_input("adventOfCode'24/day5")

small_input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

input_array = input.split("\n\n")
rules = input_array[0].split("\n")
updates = input_array[1].split("\n")


def check_rules(rules, pair):
    for rule in rules:
        if pair == rule:
            return True
    return False

def get_correct_updates(rules, updates):
    correct_updates = []
    incorrect_updates = []
    count = 0
    # Check each update
    for update in updates:
        update = update.split(",")
        update_count = 0
        # Check each page
        for ind, page in enumerate(update):
            page_count = 0
            if ind == len(update) - 1:
                update_count += 1
                if update_count == len(update):
                    correct_updates.append(update)
                else:
                    incorrect_updates.append(update)
            # Check each page with pages further
            for i in range(1, len(update) - ind + 1):
                if i == len(update) - ind:
                    if page_count == len(update) - ind - 1:
                        update_count += 1
                    continue
                check = check_rules(rules, f"{page}|{update[ind + i]}")
                if check: page_count += 1

    # Sum middle elements in array of correct updates
    for update in correct_updates:
        count += int(update[math.floor(len(update)/2)])
    #return count
    return incorrect_updates


def sort_incorrect_updates(rules, updates):
    sorted_updates = []
    count = 0
    # Check each update
    for update in updates:
        new_update = []
        for i in range(len(update)):
            new_update.append('')
        # Check each page
        for page in update:
            update_count = 0
            for rule in rules:
                if page == rule[:2] and rule[3:5] in set(update):
                    update_count += 1
            new_update[len(update) - 1 - update_count] = page
        sorted_updates.append(new_update)

    # Sum middle elements in array of sorted updates
    for update in sorted_updates:
        count += int(update[math.floor(len(update)/2)])
    return count

result = get_correct_updates(rules, updates)
result2 = sort_incorrect_updates(rules, result)
print(result2)