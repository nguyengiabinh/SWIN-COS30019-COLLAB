import queue

# represent a position in the grid with cost and heuristic information
class Node:
    def __init__(self, position, cost, heuristic):
        self.position = position
        self.cost = cost
        self.heuristic = heuristic

    # Comparison for priority queue ordering based on total cost
    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

# Heuristic function (Manhattan)
def heuristic_cost_estimate(current, goal):
    return abs(goal[0] - current[0]) + abs(goal[1] - current[1])

# Reconstruct the path from the start to the current position using the came_from dictionary
def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

def a_star_search(grid, start, goals):
    rows, columns = len(grid), len(grid[0])
    
    # Priority queue to store nodes based on their total cost
    open_set = queue.PriorityQueue()


    # Choose the goal with the minimum heuristic as the initial goal
    initial_goal = min(goals, key=lambda goal: heuristic_cost_estimate(start, goal))

    start_node = Node(start, 0, heuristic_cost_estimate(start, initial_goal))
    open_set.put(start_node)
    
    # Dictionary to store the parent of each node in the optimal path
    came_from = {}
    
    # Dictionary to store the cost of the optimal path to each node
    g_score = {start: 0}
    
    # Set to store visited nodes
    visited_set = set()

    while not open_set.empty():
        current_node = open_set.get()
        visited_set.add(current_node.position)

        if current_node.position == initial_goal:
            return reconstruct_path(came_from, current_node.position), visited_set

        # Explore neighbors
        for neighbor in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor_position = (current_node.position[0] + neighbor[0], current_node.position[1] + neighbor[1])

            # Check if the neighbor is within the grid and not an obstacle
            if 0 <= neighbor_position[0] < columns and 0 <= neighbor_position[1] < rows and grid[neighbor_position[1]][neighbor_position[0]] != 'B':
                tentative_g_score = g_score[current_node.position] + 1

                # Update if this path to the neighbor is better
                if neighbor_position not in g_score or tentative_g_score < g_score[neighbor_position]:
                    g_score[neighbor_position] = tentative_g_score
                    open_set.put(Node(neighbor_position, tentative_g_score, heuristic_cost_estimate(neighbor_position, initial_goal)))
                    came_from[neighbor_position] = current_node.position

    return None, visited_set
