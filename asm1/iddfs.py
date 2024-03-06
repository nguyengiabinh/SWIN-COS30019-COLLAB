import sys
from dfs_search import dfs_search

def iddfs_search(grid, start, goals):
    # Use sys.maxsize to represent a large integer value as the initial depth limit
    max_depth_limit = sys.maxsize

    # Iterate through depth limits starting from 0 up to max_depth_limit
    for depth_limit in range(max_depth_limit):
        # Perform depth-limited DFS search with the current depth limit
        result, visited_set = dfs_search_with_depth_limit(grid, start, goals, depth_limit)

        # If a path to any goal is found within the depth limit, return the result and visited set
        if result is not None:
            return result, visited_set

    # If no path to any goal is found within the depth limit, return None and the visited set
    return None, visited_set

def dfs_search_with_depth_limit(grid, start, goals, depth_limit):
    rows, columns = len(grid), len(grid[0])
    visited = set()

    def dfs(current_position, path, current_depth):
        visited.add(current_position)

        # If the current position is in the list of goals, return the path and visited set
        if current_position in goals:
            return path + [current_position], visited

        # If the current depth exceeds the depth limit, stop the DFS exploration
        if current_depth >= depth_limit:
            return None, visited

        # Explore neighbors within the depth limit
        for neighbor in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor_position = (current_position[0] + neighbor[0], current_position[1] + neighbor[1])

            # Check if the neighbor position is within the grid and not blocked by an obstacle
            if 0 <= neighbor_position[0] < columns and 0 <= neighbor_position[1] < rows and grid[neighbor_position[1]][neighbor_position[0]] != 'B':
                # Explore the neighbor recursively with updated depth
                if neighbor_position not in visited:
                    result, visited_set = dfs(neighbor_position, path + [current_position], current_depth + 1)
                    if result:
                        return result, visited_set

        return None, visited

    # Start the DFS search from the start position with initial depth 0
    return dfs(start, [], 0)
