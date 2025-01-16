# Shortest Path in a Grid Given a 2D grid, find the shortest path from top-left to bottom-right, moving only down or right (use BFS or DFS).
from collections import deque

def shortest_path_in_grid(grid):
    # Get the number of rows and columns
    m, n = len(grid), len(grid[0])
    
    # Directions to move: right (0, 1) and down (1, 0)
    directions = [(0, 1), (1, 0)]
    
    # Queue for BFS: stores tuples of (row, col, steps)
    queue = deque([(0, 0, 0)])  # Starting point with 0 steps
    
    # Visited set to keep track of visited positions
    visited = set()
    visited.add((0, 0))  # Mark the starting point as visited
    
    while queue:
        x, y, steps = queue.popleft()
        
        # If we reach the bottom-right corner, return the number of steps
        if x == m - 1 and y == n - 1:
            return steps
        
        # Explore the two possible directions (right and down)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # Check if the new position is within bounds and not visited
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))  # Add new position with updated steps
    
    # If there's no valid path, return -1
    return -1

# Example usage
grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]

result = shortest_path_in_grid(grid)
print("Shortest path length:", result)
