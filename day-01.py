import os

list_1 = []
list_2 = []

with open("day-01.txt", "r") as file:
    for line in file.readlines():
        first_number = int(line[0:5])
        second_number = int(line[8:13])
        list_1.append(first_number)
        list_2.append(second_number)


list_1.sort()
list_2.sort()

total_difference = 0
for pair in zip(list_1, list_2):
    x, y = pair
    diff = abs(x-y)
    total_difference += diff

print("Total Difference: ", total_difference)


occurences = {}
for number in list_2:
    if number in occurences:
        occurences[number] += 1
    else:
        occurences[number] = 1
     
similarity_score = 0
for number in list_1:
    if number not in occurences:
        score = 0
    else:
        score = number * occurences[number]
    similarity_score += score
print("Similarity score: ", similarity_score)