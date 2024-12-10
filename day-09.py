disk = []
with open('day-09.txt') as f:
    input = f.readline()
    disk = list(input.strip())

id = 0
is_file = True
individual_blocks_list = []
for val in disk:
    if is_file:
        for i in range(int(val)):
            individual_blocks_list.append(id)
        id += 1
    else:
        for i in range(int(val)):
            # Use -1 to represent empty space, can't use 0 because theres are ids
            individual_blocks_list.append(-1)
    # flip if we are in a file or empty space
    is_file = not is_file 

copy_individual_blocks_list = [val for val in individual_blocks_list]
# Now fill the empty space
while True:
    try:
        next_opening = individual_blocks_list.index(-1)
    except ValueError:
        break
    individual_blocks_list.remove(-1)
    individual_blocks_list.insert(next_opening, individual_blocks_list.pop())

# Now calculate checksum
checksum = 0
for i, val in enumerate(individual_blocks_list):
    checksum += i * val
print(checksum)

individual_blocks_list = copy_individual_blocks_list

def get_length_of_space(index, list_to_check):
    val_to_look_for = list_to_check[index]
    cur_index = index
    size = 0
    while True:
        try:
            if list_to_check[cur_index] != val_to_look_for:
                break
        except IndexError:
            break
        size += 1
        cur_index += 1
    return size


def find_free_space(index_of_to_insert, list_to_check):
    curr_index = 0
    while True:
        try:
            next_available_slot = curr_index + list_to_check[curr_index:index_of_to_insert].index(-1)
        except ValueError:
            return -1
        size_of_slot = get_length_of_space(next_available_slot, list_to_check)
        size_of_data = get_length_of_space(index_of_to_insert, list_to_check)
        if size_of_data > size_of_slot:
            curr_index = next_available_slot + 1
            continue
        return next_available_slot


ids_desc = sorted(list(set(individual_blocks_list)), reverse=True)

for id in ids_desc:
    print(id)
    location = individual_blocks_list.index(id)
    free_space = find_free_space(location, individual_blocks_list)
    if free_space == -1:
        continue

    size_of_data = get_length_of_space(location, individual_blocks_list)
    # ok now the hard part, do the swap
    for i in range(size_of_data):
        individual_blocks_list[location+i], individual_blocks_list[free_space+i] = individual_blocks_list[free_space+i], individual_blocks_list[location+i]

# Now calculate checksum
checksum = 0
for i, val in enumerate(individual_blocks_list):
    if val != -1:
        checksum += i * val
print(checksum)