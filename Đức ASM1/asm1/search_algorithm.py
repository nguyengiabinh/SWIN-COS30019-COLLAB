import math

class Search:
    def __init__(self, grid):
        self.grid = grid
        self.visited = set()
        self.search_movement = []
        self.path = []
        self.heuristicFunction = "manhattan"

    def get_visited_nodes(self):
        return self.visited

    def get_search_movement(self):
        return self.search_movement

    def is_valid_move(self, position):
        row, col = position

        # Ensure that the position is within the grid boundaries
        if row < 0 or row >= self.grid.rows or col < 0 or col >= self.grid.cols:
            return False

        # Check if the position is not inside a wall
        for wall in self.grid.walls:
            x, y, width, height = wall
            if col >= x and col < x + width and row >= y and row < y + height:
                return False

        return True

    def get_neighbors(self, position):
        row, col = position
        neighbors = [
            (row - 1, col),  # up
            (row, col - 1),  # left
            (row + 1, col),  # down
            (row, col + 1),  # right
        ]

        valid_neighbors = [neighbor for neighbor in neighbors if self.is_valid_move(neighbor)]

        return valid_neighbors

    # h(n) heuristic
    # Mahattan = |x1-x2| + |y1-y2|
    def manhattan_distance(self, position, goal):
        x1, y1 = position
        x2, y2 = goal
        return abs(x1 - x2) + abs(y1 - y2)

    # DFS
    def dfs(self, position, path, stack=None):
        if stack is None:
            stack = []

        if position in self.grid.goal_states:
            self.path = path
            return True

        self.visited.add(position)
        self.search_movement.append(position)

        for neighbor in self.get_neighbors(position):
            direction = (neighbor[0] - position[0], neighbor[1] - position[1])
            direction_map = {(-1, 0): 'up', (0, -1): 'left', (1, 0): 'down', (0, 1): 'right'}
            move_direction = direction_map[direction]
            if neighbor not in self.visited:
                stack.append(neighbor)
                if self.dfs(neighbor, path + [move_direction], stack):
                    return True
                stack.pop()
        self.visited.remove(position)
        return False

    # BFS
    def bfs(self):
        start = self.grid.start_state
        queue = [(start, [])]

        while queue:
            position, path = queue.pop(0)

            self.search_movement.append(position)

            if position in self.grid.goal_states:
                return '; '.join(path) + ';'

            if position not in self.visited:
                self.visited.add(position)

                for neighbor in self.get_neighbors(position):
                    direction = (neighbor[0] - position[0], neighbor[1] - position[1])
                    direction_map = {(-1,   0): 'up', (0, -1): 'left', (1, 0): 'down', (0, 1): 'right'}
                    move_direction = direction_map[direction]
                    queue.append((neighbor, path + [move_direction]))

        return "No path found."

    # GBFS
    def greedy_best_first_search(self):
        start = self.grid.start_state
        goal_states = self.grid.goal_states

        open_list = [(start, 0, [])]
        closed_list = set()

        while open_list:
            if not goal_states:
                return "No goals left to find."

            open_list.sort(key=lambda x: min(self.manhattan_distance(x[0], goal) for goal in goal_states))
            position, cost, path = open_list.pop(0)
            self.search_movement.append(position)

            if position in goal_states:
                return '; '.join(path) + ';'

            closed_list.add(position)
            self.visited.add(position)

            for neighbor in self.get_neighbors(position):
                if neighbor not in closed_list:
                    direction = (neighbor[0] - position[0], neighbor[1] - position[1])
                    direction_map = {(-1, 0): 'up', (0, -1): 'left', (1, 0): 'down', (0, 1): 'right'}
                    move_direction = direction_map[direction]
                    neighbor_cost = cost + 1
                    existing_neighbor = [entry for entry in open_list if entry[0] == neighbor]
                    if not existing_neighbor:
                        open_list.append((neighbor, neighbor_cost, path + [move_direction]))

        return "No path found."

    # A*
    def a_star(self):
        start = self.grid.start_state
        goal = self.grid.goal_states[0]

        open_list = [(start, 0, [])]
        closed_list = set()

        while open_list:
            open_list.sort(key=lambda x: x[1] + self.manhattan_distance(x[0], goal))
            position, cost, path = open_list.pop(0)
            self.search_movement.append(position)

            if position == goal:
                return '; '.join(path) + ';'

            closed_list.add(position)
            self.visited.add(position)

            for neighbor in self.get_neighbors(position):
                if neighbor not in closed_list:
                    direction = (neighbor[0] - position[0], neighbor[1] - position[1])
                    direction_map = {(-1, 0): 'up', (0, -1): 'left', (1, 0): 'down', (0, 1): 'right'}
                    move_direction = direction_map[direction]
                    neighbor_cost = cost + 1

                    existing_neighbor = [entry for entry in open_list if entry[0] == neighbor]
                    if not existing_neighbor or existing_neighbor[0][1] > neighbor_cost:
                        open_list.append((neighbor, neighbor_cost, path + [move_direction]))

        return "No path found."
    
    # Uniform Cost Search
    def ucs(self):
        start = self.grid.start_state
        goal_states = self.grid.goal_states

        open_list = [(start, 0, [])]
        closed_list = set()

        while open_list:
            if not goal_states:
                return "No goals left to find."

            open_list.sort(key=lambda x: x[1])
            position, cost, path = open_list.pop(0)
            self.search_movement.append(position)

            if position in goal_states:
                return '; '.join(path) + ';'

            closed_list.add(position)
            self.visited.add(position)

            for neighbor in self.get_neighbors(position):
                if neighbor not in closed_list:
                    direction = (neighbor[0] - position[0], neighbor[1] - position[1])
                    direction_map = {(-1, 0): 'up', (0, -1): 'left', (1, 0): 'down', (0, 1): 'right'}
                    move_direction = direction_map[direction]
                    neighbor_cost = cost + 1

                    existing_neighbor = [entry for entry in open_list if entry[0] == neighbor]
                    if not existing_neighbor or existing_neighbor[0][1] > neighbor_cost:
                        open_list.append((neighbor, neighbor_cost, path + [move_direction]))

        return "No path found."

    # Best First Searc
    def best_first_search(self):
        start = self.grid.start_state
        goal_states = self.grid.goal_states

        open_list = [(start, 0, [])]
        closed_list = set()

        while open_list:
            if not goal_states:
                return "No goals left to find."

            open_list.sort(key=lambda x: self.manhattan_distance(x[0], goal_states[0]))
            position, cost, path = open_list.pop(0)
            self.search_movement.append(position)

            if position in goal_states:
                return '; '.join(path) + ';'

            closed_list.add(position)
            self.visited.add(position)

            for neighbor in self.get_neighbors(position):
                if neighbor not in closed_list:
                    direction = (neighbor[0] - position[0], neighbor[1] - position[1])
                    direction_map = {(-1, 0): 'up', (0, -1): 'left', (1, 0): 'down', (0, 1): 'right'}
                    move_direction = direction_map[direction]
                    neighbor_cost = cost + 1

                    existing_neighbor = [entry for entry in open_list if entry[0] == neighbor]
                    if not existing_neighbor or existing_neighbor[0][1] > neighbor_cost:
                        open_list.append((neighbor, neighbor_cost, path + [move_direction]))

        return "No path found."


    def search(self, algorithm='dfs'):
        if algorithm == 'dfs':
            if self.dfs(self.grid.start_state, [], []):
                return '; '.join(self.path) + ';'
            else:
                return "No path found."

        elif algorithm == 'bfs':
            return self.bfs()

        elif algorithm == 'gbfs':
            return self.greedy_best_first_search()

        elif algorithm == 'a*':
            return self.a_star()

        elif algorithm == 'ucs':
            return self.ucs()

        elif algorithm == 'bestfs':
            return self.best_first_search()