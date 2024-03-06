def interpret_movements(path):
    movements = []

    # Iterate over the path to determine movements
    for i in range(1, len(path)):
        current_position = path[i - 1]
        next_position = path[i]

        x_diff = next_position[0] - current_position[0]
        y_diff = next_position[1] - current_position[1]

        # Determine the movement direction based on position differences
        if x_diff == 1:
            movements.append("Right")
        elif x_diff == -1:
            movements.append("Left")
        elif y_diff == 1:
            movements.append("Down")
        elif y_diff == -1:
            movements.append("Up")

    return movements


def count_nodes_visited(visited):
    # Count the number of nodes visited
    return len(visited)






