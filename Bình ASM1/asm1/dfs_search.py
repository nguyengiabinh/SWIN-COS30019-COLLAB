def dfs_search(grid, start, goals):
    # Get the number of rows and columns in the grid
    rows, columns = len(grid), len(grid[0])

    # Initialize a set to keep track of visited positions
    visited = set()

    # Define the order of movements (UP, LEFT, DOWN, RIGHT)
    movements = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    # Function to prioritize movements based on the defined order
    def prioritize_movements(position):
        prioritized_moves = []
        for move in movements:
            next_position = (position[0] + move[0], position[1] + move[1])

            # Check if the next position is within the grid and not an obstacle ('B')
            if 0 <= next_position[0] < columns and 0 <= next_position[1] < rows and grid[next_position[1]][next_position[0]] != 'B':
                prioritized_moves.append(next_position)
        return prioritized_moves

    # Recursive depth-first search function
    def dfs(current_position, path):
        # Mark the current position as visited
        visited.add(current_position)

        # If the current position is in the list of goals, return the path and visited set
        if current_position in goals:
            return path + [current_position], visited

        # Explore neighbors in the prioritized order
        for neighbor_position in prioritize_movements(current_position):
            if neighbor_position not in visited:
                result, visited_set = dfs(neighbor_position, path + [current_position])
                
                # If the goal is found in the recursive call, return the result
                if result:
                    return result, visited_set

        return None, visited

    # Start the depth-first search from the given start position
    return dfs(start, [])

