import re

rules = []
updates = []

with open ("day-05.txt") as file:
    in_second_section = False
    for line in file.readlines():
        if line == "\n":
            in_second_section = True
            continue
        if in_second_section:
            updates.append(
                line.strip().split(',')
            )
        else:
            rules.append(
                line.strip().split("|")
            )

def check_rule(rule, update):
    index_before = update.index(rule[0]) 
    try:
        index_after = update.index(rule[1])
    except ValueError:
        # If the second page isn't in the update, we ignore the rule
        # so return True
        return True

    return index_after > index_before


def is_valid_update(update):
    for page in update:
        for rule in rules:
            if rule[0] == page:
                if check_rule(rule, update) == False:
                    return False
    return True




valid_updates = [update for update in updates if is_valid_update(update)]

print(valid_updates)


page_sums = 0
for update in valid_updates:
    page_sums += int(update[len(update) // 2])
print(page_sums)


invalid_updates = [update for update in updates if not is_valid_update(update)]


corrected_updates = []
for invalid_update in invalid_updates:
    corrected_update = [invalid_update.pop()]
    while(invalid_update):
        next_page = invalid_update.pop()
        slots_to_try = len(corrected_update)+1
        for i in range(slots_to_try):
            corrected_update.insert(i, next_page)
            if is_valid_update(corrected_update):
                break
            else:
                corrected_update.remove(next_page)
    corrected_updates.append(corrected_update) 
print(corrected_updates)

page_sums_corrected = 0
for update in corrected_updates:
    page_sums_corrected += int(update[len(update) // 2])
print(page_sums_corrected)
