def get_movement_directions(path):
    directions = []

    for i in range(1, len(path)):
        current_pos = path[i - 1]
        next_pos = path[i]

        x_diff = next_pos[0] - current_pos[0]
        y_diff = next_pos[1] - current_pos[1]

        if x_diff == 1:
            directions.append("Right")
        elif x_diff == -1:
            directions.append("Left")
        elif y_diff == 1:
            directions.append("Down")
        elif y_diff == -1:
            directions.append("Up")

    return directions


def get_visited_node_count(visited):
    return len(visited)
