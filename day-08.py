from itertools import combinations


def in_bounds(point, grid):
    rows = len(grid)
    cols = len(grid[0])

    x, y = point
    if x >= 0 and x < rows and y >= 0 and y < cols:
        return True
    return False

def get_antinodes(p1, p2, grid):
    local_anti_nodes = []
    x1, y1 = p1
    x2, y2 = p2
    dx = x2 - x1
    dy = y2 - y1

    new_node = (x1-dx, y1-dy)
    while(in_bounds(new_node, grid)):
        local_anti_nodes.append(new_node)
        new_x, new_y = new_node
        new_node = (new_x-dx, new_y-dy)

    new_node = (x2+dx, y2+dy)
    while(in_bounds(new_node, grid)):
        local_anti_nodes.append(new_node)
        new_x, new_y = new_node
        new_node = (new_x+dx, new_y+dy)

    return local_anti_nodes

grid = []
with open('day-08.txt') as f:
    lines = f.readlines()
    for line in lines:
        grid.append(list(line.strip()))

node_to_location = {}
for i in range(len(grid)):
    for j in range(len(grid[0])):
        thing_at_grid = grid[i][j]
        if thing_at_grid == '.':
            continue
        else:
            if thing_at_grid in node_to_location:
                node_to_location[thing_at_grid].append((i, j))
            else:
                node_to_location[thing_at_grid] = [(i,j)]

antinodes = [['.' for _ in range(len(grid[0]))] for _ in range(len(grid))]



# Lets fill in the antinodes now
# loop through unique nodes
for node in node_to_location:
    # get list of all the locations of this node

    # now we need to 
    # - check all the combinations of the locations
    # - form a line between the two points
    # - extend along that line in both directions twice the distance between the points
    
    locations = node_to_location[node]
    pair_of_locations = list(combinations(locations, 2))
    for pair in pair_of_locations:
        p1, p2 = sorted(pair)
        new_antinodes = get_antinodes(p1, p2, grid)
        for new_x, new_y in new_antinodes:
            antinodes[new_x][new_y] = '#'

# now check for nodes which have multiple locations since they form an antinode
for node in node_to_location:
    locations = node_to_location[node]
    if len(locations) > 1:
        for x, y in locations:
            antinodes[x][y] = '#'



count = 0
for row in antinodes:
    for cell in row:
        if cell == '#':
            count += 1
print(count)
