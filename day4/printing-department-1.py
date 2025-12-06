def read_file(filename):
    with open(filename, "r") as f:
        grid = [line.strip() for line in f.readlines()]
    return grid

input = read_file("input.txt")

def countRollLocation(grid):
    rows = len(grid)
    cols = len(grid[0])

    # Directions around a cell (8 neighbors)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    count = 0
    # Loop through every cell in the grid
    for r in range(rows):
        for c in range(cols):
            # Only care about rolls of paper
            if grid[r][c] != '@':
                continue
            # Count neighboring rolls around this '@'
            neighbor_rolls = 0
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                # Check boundaries
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == '@':
                        neighbor_rolls += 1
            # mark if fewer than 4 neighbors
            if neighbor_rolls < 4:
                count += 1
    return count

inputEx = [
'..@@.@@@@.',
'@@@.@.@.@@',
'@@@@@.@.@@',
'@.@@@@..@.',
'@@.@@@@.@@',
'.@@@@@@@.@',
'.@.@.@.@@@',
'@.@@@.@@@@',
'.@@@@@@@@.',
'@.@.@@@.@.'
]

print(countRollLocation(inputEx))
# print(countRollLocation(input))