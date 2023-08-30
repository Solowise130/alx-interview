#!/usr/bin/python3

def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.

    Args:
        grid (List[List[int]]): A grid representing the island.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Each land cell contributes 4 to the perimeter
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Subtract 2 if there's a land cell above
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Subtract 2 if there's a land cell to the left
    
    return perimeter

# Example usage
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]
perimeter = island_perimeter(grid)
print(f"The perimeter of the island is: {perimeter}")
