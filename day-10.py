topo_map = []
with open('day-10.txt') as file:
    lines = file.readlines()
    for line in lines:
        topo_map.append([int(val) for val in line.strip()])


def find_trail_head_locations(grid):
    locations = []
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == 0:
                locations.append((i, j))
    return locations

trailheads = find_trail_head_locations(topo_map)

def get_valid_routes(location, grid):
    valid_routes = []
    x, y = location
    if x != 0:
        to_check = grid[x-1][y]
        if to_check == grid[x][y] + 1:
            valid_routes.append((x-1, y))
    try:
        to_check = grid[x+1][y]
        if to_check == grid[x][y] + 1:
            valid_routes.append((x+1, y))
    except:
        pass
    if y != 0:
        to_check = grid[x][y-1]
        if to_check == grid[x][y] + 1:
            valid_routes.append((x, y-1))
    try:
        to_check = grid[x][y+1]
        if to_check == grid[x][y] + 1:
            valid_routes.append((x, y+1))
    except:
        pass
    return valid_routes


def find_number_of_paths(start_location, topo_map):
    number_of_paths = 0
    seen_paths = set()
    to_visit = [start_location]
    while len(to_visit) > 0:   
        new_location = to_visit.pop(-1)
        x, y = new_location
        if topo_map[x][y] == 9:
            if new_location not in seen_paths:
                number_of_paths += 1
                seen_paths.add(new_location)
            continue
        valid_routes = get_valid_routes(new_location, topo_map)
        if len(valid_routes) > 0:
            for route in valid_routes:
                to_visit.append(route)
    return number_of_paths


sum_paths = 0
for trailhead in trailheads:
    number_of_paths = find_number_of_paths(trailhead, topo_map)
    sum_paths += number_of_paths
print(sum_paths)




def find_number_of_distinct_paths(start_location, topo_map):
    number_of_paths = 0
    seen_paths = set()
    to_visit = [start_location]
    multiple_times_hit = 0
    while len(to_visit) > 0:   
        new_location = to_visit.pop(-1)
        x, y = new_location
        if topo_map[x][y] == 9:
            if new_location not in seen_paths:
                number_of_paths += 1
                seen_paths.add(new_location)
            else:
                multiple_times_hit += 1
            continue
        valid_routes = get_valid_routes(new_location, topo_map)
        if len(valid_routes) > 0:
            for route in valid_routes:
                to_visit.append(route)
    return multiple_times_hit + number_of_paths


sum_paths = 0
for trailhead in trailheads:
    number_of_paths = find_number_of_distinct_paths(trailhead, topo_map)
    sum_paths += number_of_paths
print(sum_paths)