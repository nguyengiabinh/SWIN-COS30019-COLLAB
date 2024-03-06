import matplotlib.pyplot as plt
import matplotlib.patches as patches


def create_grid_map(file_path):
    rows, columns = 0, 0
    start_position = ()
    goal_positions = []
    obstacles = []

    with open(file_path, 'r') as file:
        lines = file.readlines()

        size_line = lines[0].strip()[1:-1]
        rows, columns = map(int, size_line.split(','))

        start_position_line = lines[1].strip()[1:-1]
        start_position = tuple(map(int, start_position_line.split(',')))

        goal_positions_line = lines[2].strip()
        goal_positions = [tuple(map(int, goal.strip()[1:-1].split(','))) for goal in goal_positions_line.split('|')]

        for obstacle_line in lines[3:]:
            obstacle_line = obstacle_line.strip()
            if '|' in obstacle_line:
                obstacles.extend([tuple(map(int, part.strip()[1:-1].split(','))) for part in obstacle_line.split('|')])
            else:
                obstacle = tuple(map(int, obstacle_line.replace('(', '').replace(')', '').split(',')))
                if len(obstacle) == 2:
                    obstacles.append(obstacle)
                elif len(obstacle) == 4:
                    obstacles.append(obstacle)
                else:
                    raise ValueError("Invalid obstacle format")

    grid_map = [[' ' for _ in range(columns)] for _ in range(rows)]
    grid_map[start_position[1]][start_position[0]] = 'R'

    for x, y in goal_positions:
        grid_map[y][x] = 'G'

    for x, y, w, h in obstacles:
        for i in range(h):
            for j in range(w):
                grid_map[y + i][x + j] = 'B'

    return grid_map, start_position, goal_positions, obstacles

def draw_map(grid, start, goals, obstacles, paths=None, visited=None):
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_aspect('equal')  
    total_rows = len(grid)
    
    # Draw obstacles and other elements
    for y in range(total_rows):
        for x in range(len(grid[0])):
            inverted_y = total_rows - 1 - y  
            if grid[y][x] == 'B':
                ax.add_patch(patches.Rectangle((x, inverted_y), 1, 1, edgecolor='black', facecolor='gray'))
            elif grid[y][x] == 'R':
                plt.plot(x + 0.5, inverted_y + 0.5, 'ro', markersize=20, label='Start')
            elif grid[y][x] == 'G':
                plt.plot(x + 0.5, inverted_y + 0.5, 'go', markersize=20, label='Goal')
    
    # Draw visited cells if provided
    if visited:
        for col, row in visited:
            plt.plot(col + 0.5, total_rows - 1 - row + 0.5, 'blue', marker='o', markersize=10)
    
    if paths:
        for col,row in paths:
            plt.plot(col + 0.5, total_rows - 1 - row + 0.5, 'yellow', marker='o', markersize=10)
            
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.xticks(range(len(grid[0])))
    plt.yticks(range(total_rows))
    plt.xlabel("X", fontsize=14)
    plt.ylabel("Y", fontsize=14)
    plt.title("Robot Map", fontsize=16)
    plt.legend()
    plt.show()
