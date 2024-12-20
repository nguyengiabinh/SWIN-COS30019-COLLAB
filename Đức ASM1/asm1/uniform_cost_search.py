import math

class Node:
    def __init__(self, position, cost, heuristic):
        self.position = position
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return self.cost < other.cost
    
    """
    Uniform Cost Search algorithm implementation.
    
    Parameters:
    - grid (list): The grid representing the map.
    - start (tuple): The starting position.
    - goal (tuple): The goal position.
    
    Returns:
    - path (list): The path from start to goal.
    - visited_nodes (set): Set of visited nodes during the search.
    """

def ucs_search(grid, start, goals):  
    rows, columns = len(grid), len(grid[0])
    open_set = []
    
    initial_goal = min(goals, key=lambda goal: heuristic_cost_estimate(start, goal))

    start_node = Node(start, 0, heuristic_cost_estimate(start, initial_goal))
    open_set.append(start_node)
    came_from = {}
    g_score = {start: 0}
    visited_nodes = set()

    while open_set:
        open_set.sort(key=lambda x: x.cost)
        current_node = open_set.pop(0)
        visited_nodes.add(current_node.position)

        if current_node.position in goals:
            return reconstruct_path(came_from, current_node.position), visited_nodes

        for neighbor in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor_position = (current_node.position[0] + neighbor[0], current_node.position[1] + neighbor[1])

            if 0 <= neighbor_position[0] < columns and 0 <= neighbor_position[1] < rows and grid[neighbor_position[1]][neighbor_position[0]] != 'B':
                tentative_g_score = g_score[current_node.position] + 1

                if neighbor_position not in g_score or tentative_g_score < g_score[neighbor_position]:
                    g_score[neighbor_position] = tentative_g_score
                    neighbor_node = Node(neighbor_position, tentative_g_score, heuristic_cost_estimate(neighbor_position,initial_goal))
                    open_set.append(neighbor_node)
                    came_from[neighbor_position] = current_node.position

    return None, visited_nodes

def heuristic_cost_estimate(current, goal):
    return abs(goal[0] - current[0]) + abs(goal[1] - current[1])

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]
