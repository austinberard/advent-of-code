from itertools import product

list_of_sums = []
list_of_nums = []
with open('day-07.txt') as file:
    for line in file.readlines():
        sum, numbers = line.split(':')
        numbers = numbers.strip().split(' ')
        list_of_sums.append(sum) 
        list_of_nums.append(numbers)
    

def evaluate_expression(numbers, operators):
    expression = ""
    expression = []
    for number, operator in zip(numbers, operators):
        expression.append(number)
        expression.append(operator)
    expression.append(numbers[-1])
    # Now we have a list expression like this
    # [10, +, 19, *, 20]
    # And we want to evaluate left to right
    while(len(expression)>2):
        num = int(expression.pop(0))
        operator = expression.pop(0)
        num_2 = int(expression.pop(0))
        if operator == '+':
            val = num + num_2
        elif operator == '*':
            val = num * num_2
        elif operator == '||':
            val = int(str(num) + str(num_2))
        expression.insert(0, val)

    return expression[0]
        

total_sum = 0
for sum, nums in zip(list_of_sums, list_of_nums):
    times = len(nums) - 1
    options = ['+', '*']
    to_try = combinations = list(product(options, repeat=times))
    for combo in to_try:
        if int(sum) == evaluate_expression(nums, combo):
            print("Match")
            print(nums, combo)
            total_sum += int(sum)
            break
print(total_sum)




total_sum_part2 = 0
for sum, nums in zip(list_of_sums, list_of_nums):
    times = len(nums) - 1
    options = ['+', '*', '||']
    to_try = combinations = list(product(options, repeat=times))
    for combo in to_try:
        if int(sum) == evaluate_expression(nums, combo):
            print("Match")
            print(nums, combo)
            total_sum_part2 += int(sum)
            break
print(total_sum_part2)