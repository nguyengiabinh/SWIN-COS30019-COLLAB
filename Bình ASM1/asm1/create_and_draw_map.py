import matplotlib.pyplot as plt

def create_grid_map(file_path):
    # Initialize variables to store map information
    rows, columns = 0, 0
    start_position = ()
    goal_positions = []
    obstacles = []

    # Read map information from the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

        # Parse map size
        size_line = lines[0].strip()[1:-1]
        rows, columns = map(int, size_line.split(','))

        # Parse start position
        start_position_line = lines[1].strip()[1:-1]
        start_position = tuple(map(int, start_position_line.split(',')))

        # Parse goal positions
        goal_positions_line = lines[2].strip()
        goal_positions = [tuple(map(int, goal.strip()[1:-1].split(','))) for goal in goal_positions_line.split('|')]

        # Parse obstacles
        for obstacle_line in lines[3:]:
            obstacle_line = obstacle_line.strip()

            if '|' in obstacle_line:
                obstacles.extend([tuple(map(int, part.strip()[1:-1].split(','))) for part in obstacle_line.split('|')])
            else:
                obstacle = tuple(map(int, obstacle_line.replace('(', '').replace(')', '').split(',')))

                # Check obstacle format and add to the list
                if len(obstacle) == 2:
                    obstacles.append(obstacle)
                elif len(obstacle) == 4:
                    obstacles.append(obstacle)
                else:
                    raise ValueError("Invalid obstacle format")

    # Create a 2D grid map with default values
    grid_map = [[' ' for _ in range(columns)] for _ in range(rows)]

    # Mark start position with 'R'
    grid_map[start_position[1]][start_position[0]] = 'R'

    # Mark goal positions with 'G'
    for idx, (x, y) in enumerate(goal_positions):
        goal_marker = f'G{idx + 1}'
        grid_map[y][x] = goal_marker

    # Mark obstacle positions with 'B'
    for x, y, w, h in obstacles:
        for i in range(h):
            for j in range(w):
                grid_map[y + i][x + j] = 'B'

    return grid_map, start_position, goal_positions, obstacles

def draw_map(grid, start, goals, obstacles, path=None, visited=None):
    # Plot each cell in the grid based on its content
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'B':
                plt.plot(col + 0.5, row + 0.5, 'brown', marker='s', markersize=10)
            elif grid[row][col] == 'R':
                plt.plot(col + 0.5, row + 0.5, 'red', marker='o', markersize=15)
            elif 'G' in grid[row][col]:
                plt.plot(col + 0.5, row + 0.5, 'green', marker='o', markersize=15, label=grid[row][col])
            elif visited and (col, row) in visited:
                plt.plot(col + 0.5, row + 0.5, 'orange', marker='o', markersize=10)  # Orange circle for visited

    # If there is a path, plot it with purple circles
    if path:
        for col, row in path:
            plt.plot(col + 0.5, row + 0.5, 'purple', marker='o', markersize=10)

    # Set plot properties
    plt.xlim(-0.5, len(grid[0]) - 0.5)
    plt.ylim(-0.5, len(grid) - 0.5)
    plt.gca().invert_yaxis()
    plt.grid(True)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Grid Map")
    plt.legend()
    plt.show()