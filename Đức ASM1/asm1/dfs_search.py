# dfs_search.py

def asm1_dfs(grid, start, goal):  # Đổi tên hàm thành custom_dfs
    rows, columns = len(grid), len(grid[0])
    visited_nodes = set()
    
    def prioritize(position):
        prioritized_moves = []
        for move in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            next_position = (position[0] + move[0], position[1] + move[1])
            if 0 <= next_position[0] < columns and 0 <= next_position[1] < rows and grid[next_position[1]][next_position[0]] != 'B':
                prioritized_moves.append(next_position)
        return prioritized_moves


    def dfs(current_position, path):
        visited_nodes.add(current_position)

        if current_position == goal:
            return path + [current_position], visited_nodes

        for neighbor_position in prioritize(current_position):
            if neighbor_position not in visited_nodes:
                result, visited_set = dfs(neighbor_position, path + [current_position])
                if result:
                    return result, visited_set

        return None, visited_nodes

    return dfs(start, [])
