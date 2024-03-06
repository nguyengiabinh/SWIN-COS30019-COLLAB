from collections import deque

def bfs_search(grid, start, goals):
    rows, columns = len(grid), len(grid[0])
    visited = set()  # Store visited positions
    queue = deque([(start, [])])  # Initialize the queue with the starting position and an empty path
    visited_set = set()  # Store visited positions

    while queue:
        # Dequeue the front node
        current_position, path = queue.popleft()
        visited_set.add(current_position)

        # Goal found, return the path and visited set
        if current_position in goals:
            return path + [current_position], visited_set

        # Mark the current position as visited
        if current_position not in visited:
            visited.add(current_position)

            # Explore neighbors
            for neighbor in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                neighbor_position = (current_position[0] + neighbor[0], current_position[1] + neighbor[1])

                # Check if the neighbor is within the grid and not an obstacle
                if 0 <= neighbor_position[0] < columns and 0 <= neighbor_position[1] < rows and grid[neighbor_position[1]][neighbor_position[0]] != 'B':
                    # Enqueue the neighbor with an updated path
                    queue.append((neighbor_position, path + [current_position]))

    return None, visited_set
