def read_file(filename):
    with open(filename, "r") as f:
        grid = [line.strip() for line in f.readlines()]
    return grid

input = read_file("input.txt")

def count_total_removed(grid):
    rows = len(grid)
    cols = len(grid[0])

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    # Convert to mutable grid
    g = [list(row) for row in grid]

    total_removed = 0

    while True:
        to_remove = []

        # Step 1: find all accessible rolls
        for r in range(rows):
            for c in range(cols):
                if g[r][c] != '@':
                    continue

                neighbor_rolls = 0

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                         if g[nr][nc] == '@':
                            neighbor_rolls += 1

                if neighbor_rolls < 4:
                    to_remove.append((r, c))

        # Step 2: if none are accessible → stop
        if not to_remove:
            break

        # Step 3: remove them
        for r, c in to_remove:
            g[r][c] = '.'

        total_removed += len(to_remove)

    return total_removed

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

# print(count_total_removed(inputEx))
print(count_total_removed(input))