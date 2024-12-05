import re

def get_all_diagonals(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    diagonals = []
    
    for start_row in range(rows-1, -1, -1):
        diagonal = []
        r, c = start_row, 0
        while r < rows and c < cols:
            diagonal.append(matrix[r][c])
            r += 1
            c += 1
        diagonals.append(diagonal)
    
    for start_col in range(1, cols):
        diagonal = []
        r, c = 0, start_col
        while r < rows and c < cols:
            diagonal.append(matrix[r][c])
            r += 1
            c += 1
        diagonals.append(diagonal)
    
    for start_col in range(cols):
        diagonal = []
        r, c = 0, start_col
        while r < rows and c >= 0:
            diagonal.append(matrix[r][c])
            r += 1
            c -= 1
        if len(diagonal) > 1:
            diagonals.append(diagonal)
    
    for start_row in range(1, rows):
        diagonal = []
        r, c = start_row, cols-1
        while r < rows and c >= 0:
            diagonal.append(matrix[r][c])
            r += 1
            c -= 1
        if len(diagonal) > 1:
            diagonals.append(diagonal)
            
    return diagonals

grid = []
with open("day-04.txt") as f:
    for line in f.readlines():
        row = []
        for ch in line.strip():
            row.append(ch)
        grid.append(row)

rows = []
for row in grid:
    rows.append("".join(row))

cols_temp = [list(col) for col in zip(*grid)]
cols = []
for col in cols_temp:
    cols.append("".join(col))


diagnols_temp = get_all_diagonals(grid)
diagnols = []
for diag in diagnols_temp:
    diagnols.append("".join(diag))

rows_reversed = []
for row in rows:
    rows_reversed.append(row[::-1])

cols_reversed = []
for col in cols:
    cols_reversed.append(col[::-1])

diagnols_reversed = []
for diag in diagnols:
    diagnols_reversed.append(diag[::-1])

everything = []
everything.extend(rows)
everything.extend(rows_reversed)
everything.extend(cols)
everything.extend(cols_reversed)
everything.extend(diagnols)
everything.extend(diagnols_reversed)

print(everything)

pattern = r"XMAS"
count = 0
for thing in everything:
    matches = re.findall(pattern, thing) 
    count += len(matches)
print(count)