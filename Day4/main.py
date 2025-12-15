with open("input.in") as f:
    grid = [list(line.strip()) for line in f if line.strip()]
ROWS = len(grid)
COLS = len(grid[0])
NEIGHBORS = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1)
]
def count_adjacent(grid, r, c):
    count = 0
    for dr, dc in NEIGHBORS:
        nr, nc = r + dr, c + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS:
            if grid[nr][nc] == "@":
                count += 1
    return count
part1 = 0
for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c] == "@":
            if count_adjacent(grid, r, c) < 4:
                part1 += 1
print("Part 1 solution:", part1)
from copy import deepcopy
grid2 = deepcopy(grid)
total_removed = 0
while True:
    to_remove = []
    for r in range(ROWS):
        for c in range(COLS):
            if grid2[r][c] == "@":
                if count_adjacent(grid2, r, c) < 4:
                    to_remove.append((r, c))
    if not to_remove:
        break
    for r, c in to_remove:
        grid2[r][c] = "."
    total_removed += len(to_remove)
print("Part 2 solution:", total_removed)
