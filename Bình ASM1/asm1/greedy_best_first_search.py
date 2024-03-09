import queue

# Represent a position in the grid with heuristic information
class Node:
    def __init__(self, position, heuristic):
        self.position = position
        self.heuristic = heuristic

    # Comparison for priority queue ordering based on heuristic
    def __lt__(self, other):
        return self.heuristic < other.heuristic

# Heuristic function (Manhattan)
def heuristic_cost_estimate(current, goal):
    return abs(goal[0] - current[0]) + abs(goal[1] - current[1])

# Explore neighbors for a given node
def explore_neighbors(grid, current_node, visited_set, came_from, initial_goal):
    rows, columns = len(grid), len(grid[0])
    neighbors = []

    # Prioritize neighbors in the order: up, left, down, right
    movements = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    for movement in movements:
        neighbor_position = (
            current_node.position[0] + movement[0], current_node.position[1] + movement[1]
        )

        # Check if the neighbor is within the grid and not an obstacle
        if (
            0 <= neighbor_position[0] < columns
            and 0 <= neighbor_position[1] < rows
            and grid[neighbor_position[1]][neighbor_position[0]] != "B"
        ):
            neighbor_node = Node(
                neighbor_position, heuristic_cost_estimate(neighbor_position, initial_goal)
            )
            neighbors.append(neighbor_node)

    # Sort neighbors based on movement priority: up, left, down, right
    neighbors.sort(
        key=lambda x: movements.index(
            (x.position[0] - current_node.position[0], x.position[1] - current_node.position[1])
        )
    )

    return neighbors

def greedy_best_first_search(grid, start, goals):

    # Priority queue to store nodes based on their heuristic
    open_set = queue.PriorityQueue()

    # Choose the goal with the minimum heuristic as the initial goal
    initial_goal = min(goals, key=lambda goal: heuristic_cost_estimate(start, goal))

    start_node = Node(start, heuristic_cost_estimate(start, initial_goal))
    open_set.put(start_node)

    # Dictionary to store the parent of each node in the optimal path
    came_from = {start: None}

    # Set to store visited nodes
    visited_set = set()

    while not open_set.empty():
        current_node = open_set.get()
        visited_set.add(current_node.position)

        if current_node.position in goals:
            return reconstruct_path(came_from, current_node.position), visited_set

        # Explore neighbors
        neighbors = explore_neighbors(grid, current_node, visited_set, came_from, initial_goal)

        # Update the optimal path
        for neighbor in neighbors:
            if (
                neighbor.position not in visited_set
                and neighbor.position not in came_from
            ):
                open_set.put(neighbor)
                came_from[neighbor.position] = current_node.position

    return None, visited_set

# Reconstruct the path from the start to the current position using the came_from dictionary
def reconstruct_path(came_from, current):
    path = []
    while current:
        path.append(current)
        current = came_from[current]
    return path[::-1]





