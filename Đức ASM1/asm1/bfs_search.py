from collections import deque

def asm1_bfs(grid, start, goal):  
    rows, columns = len(grid), len(grid[0])
    visited_nodes = set()  
    queue = deque([(start, [])])
    visited_set = set()

    while queue:
        current_pos, path = queue.popleft()
        visited_set.add(current_pos)

        if current_pos == goal:
            return path + [current_pos], visited_set

        if current_pos not in visited_nodes:  
            visited_nodes.add(current_pos)  

            for neighbor in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                neighbor_pos = (current_pos[0] + neighbor[0], current_pos[1] + neighbor[1])

                if 0 <= neighbor_pos[0] < columns and 0 <= neighbor_pos[1] < rows and grid[neighbor_pos[1]][neighbor_pos[0]] != 'B':
                    queue.append((neighbor_pos, path + [current_pos]))

    return None, visited_set
