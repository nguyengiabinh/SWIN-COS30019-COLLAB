def asm1_dfs(grid, start, goal):  
    """
    Depth-First Search algorithm implementation.
    
    Parameters:
    - grid (list): The grid representing the map.
    - start (tuple): The starting position.
    - goal (tuple): The goal position.
    
    Returns:
    - path (list): The path from start to goal.
    - visited_nodes (set): Set of visited nodes during the search.
    """
    rows, columns = len(grid), len(grid[0])
    visited_nodes = set()
    
    def prioritize(position):
        prioritized_moves = []
        for move in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            next_position = (position[0] + move[0], position[1] + move[1])
            if 0 <= next_position[0] < columns and 0 <= next_position[1] < rows and grid[next_position[1]][next_position[0]] != 'B':
                prioritized_moves.append(next_position)
        return prioritized_moves

    def dfs(current_position, path, stack=None):
        if stack is None:
            stack = []

        visited_nodes.add(current_position)

        if current_position in goal:
            return path + [current_position], visited_nodes

        for neighbor_position in prioritize(current_position):
            if neighbor_position not in visited_nodes:
                stack.append(neighbor_position)
                result, visited_set = dfs(neighbor_position, path + [current_position], stack)
                if result:
                    return result, visited_set
                stack.pop()

        return None, visited_nodes

    return dfs(start, [], [])

