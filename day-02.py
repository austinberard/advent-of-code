import re
levels = []
with open("day-02.txt") as file:
    for line in file.readlines():
        levels.append([int(x) for x in re.findall(r'-?\d+', line)])

def check_level(level):
    increasing = True
    if level[1] < level[0]:
        increasing = False
    prev_number = None
    for number in level:
        if prev_number == None:
            prev_number = number
            continue
        else:
            if increasing:
                if prev_number < number <= prev_number + 3:
                    pass
                else:
                    return False
            else:
                if prev_number > number >= prev_number - 3:
                    pass
                else:
                    return False
        prev_number = number

    return True

             
safe_reports = 0
for level in levels:
    if check_level(level):
        safe_reports += 1
    else:
        levels_sans_one = [level[:i] + level[i+1:] for i in range(len(level))]
        if any([check_level(level_sans_one) for level_sans_one in levels_sans_one]):
            safe_reports += 1


print("Safe reports: ", safe_reports)