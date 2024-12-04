import re

mul_pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
matches = []
with open("day-03.txt") as f:
    for line in f.readlines():
        matches.extend([match for match in re.findall(mul_pattern, line)])

sum = 0
for match in matches:
    x, y = re.findall(r"[0-9]{1,3}", match)
    sum += int(x) * int(y)
print(sum) 


sum_2 = 0
mul_do_dont_pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)"
part_2_matches = []
with open("day-03.txt") as f:
    for line in f.readlines():
        part_2_matches.extend(re.findall(mul_do_dont_pattern, line))

skip = False
for match in part_2_matches:
    if match == "don't()":
        skip = True
        continue
    if match == "do()":
        skip = False
        continue
    if skip:
        continue
    else:
        x, y = re.findall(r"[0-9]{1,3}", match)
        sum_2 += int(x) * int(y)
print(sum_2)
                
        