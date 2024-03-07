
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
