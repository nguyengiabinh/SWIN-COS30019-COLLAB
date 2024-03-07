import heapq
import math

def heuristic_cost_estimate(current, goal):
    return abs(goal[0] - current[0]) + abs(goal[1] - current[1])

def asm1_gdf_search(grid, start, goals):  
    
    rows, columns = len(grid), len(grid[0])
    visited_nodes = set()
    priority_queue = []
    came_from = {}
    
    # Tìm mục tiêu gần nhất
    initial_goal = min(goals, key=lambda goal: heuristic_cost_estimate(start, goal))

    heapq.heappush(priority_queue, (0, start))
    
    def heuristic(position):
        return abs(position[0] - initial_goal[0]) + abs(position[1] - initial_goal[1])

    def sort_key(neighbor):
        x, y = neighbor
        heuristic_value = heuristic(neighbor)
        return (heuristic_value, x, y) 

    while priority_queue:
        current_cost, current_position = heapq.heappop(priority_queue)

        if current_position == initial_goal:
            path = reconstruct_path(current_position, came_from)
            return path, visited_nodes

        if current_position not in visited_nodes:
            visited_nodes.add(current_position)

            neighbors = get_neighbors(current_position, grid, rows, columns)
            neighbors.sort(key=sort_key)

            for neighbor_position in neighbors:
                if neighbor_position not in visited_nodes:
                    neighbor_cost = current_cost + 1  # Cost của mỗi bước là 1
                    heapq.heappush(priority_queue, (neighbor_cost, neighbor_position))
                    came_from[neighbor_position] = current_position

    return None, visited_nodes

def reconstruct_path(goal, came_from):
    path = [goal]
    while came_from.get(path[-1]):
        path.append(came_from[path[-1]])
    return path[::-1]

def get_neighbors(position, grid, rows, columns):
    neighbors = []
    for move in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
        neighbor_position = (position[0] + move[0], position[1] + move[1])
        if 0 <= neighbor_position[0] < columns and 0 <= neighbor_position[1] < rows and grid[neighbor_position[1]][neighbor_position[0]] != 'B':
            neighbors.append(neighbor_position)
    return neighbors
