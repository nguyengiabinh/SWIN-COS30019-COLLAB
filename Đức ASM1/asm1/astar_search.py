import queue

class Node:
    def __init__(self, position, cost, heuristic):
        self.position = position
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def asm1_a_star_search(grid, start, goals):  
    """
    A* search algorithm implementation.
    
    Parameters:
    - grid (list): The grid representing the map.
    - start (tuple): The starting position.
    - goals (list): List of goal positions.
    
    Returns:
    - path (list): The path from start to goal.
    - visited_nodes (set): Set of visited nodes during the search.
    """
    rows, columns = len(grid), len(grid[0])
    open_set = queue.PriorityQueue()
    
    initial_goal = min(goals, key=lambda goal: heuristic_cost_estimate(start, goal))

    start_nodes = Node(start, 0, heuristic_cost_estimate(start, initial_goal))
    open_set.put(start_nodes)
    came_from = {}
    g_score = {start: 0}
    visited_nodes = set()

    while not open_set.empty():
        current_node = open_set.get()
        visited_nodes.add(current_node.position)

        if current_node.position == initial_goal:
            return reconstruct_path(came_from, current_node.position), visited_nodes

        for neighbor in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor_position = (current_node.position[0] + neighbor[0], current_node.position[1] + neighbor[1])

            if 0 <= neighbor_position[0] < columns and 0 <= neighbor_position[1] < rows and grid[neighbor_position[1]][neighbor_position[0]] != 'B':
                tentative_g_score = g_score[current_node.position] + 1

                if neighbor_position not in g_score or tentative_g_score < g_score[neighbor_position]:
                    g_score[neighbor_position] = tentative_g_score
                    open_set.put(Node(neighbor_position, tentative_g_score, heuristic_cost_estimate(neighbor_position, initial_goal)))
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
