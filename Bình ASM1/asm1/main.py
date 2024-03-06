from create_and_draw_map import create_grid_map, draw_map
from weighted_astar import a_star_search_weighted
from astar_search import a_star_search
from bfs_search import bfs_search
from dfs_search import dfs_search
from greedy_best_first_search import greedy_best_first_search
from iddfs import iddfs_search  
from tree_interpreter import interpret_movements, count_nodes_visited
import os

def main():
    # Get the file path from the user
    while True:
        file_path = input("Enter the file path: ")

        if os.path.exists(file_path):
            break
        else:
            print(f"The file '{file_path}' does not exist. Please enter a valid file path.")

    # Define available search algorithms
    algorithms = ['astar', 'bfs', 'dfs', 'gbfs', 'iddfs', 'astar_weighted']

    # Get the desired search algorithm from the user
    while True:
        search_algorithm = input("Enter the search algorithm ('astar', 'bfs', 'dfs', 'gbfs', 'iddfs', 'astar_weighted'): ")

        if search_algorithm in algorithms:
            print(f"Chosen search algorithm: {search_algorithm}")
            break
        else:
            print("Invalid search algorithm. Please enter a valid search algorithm.")

    # Create the grid map, start position, goal positions, and obstacles
    grid_map, start_position, goal_positions, obstacles = create_grid_map(file_path)
    draw_map(grid_map, start_position, goal_positions, obstacles)

    # Perform the selected search algorithm
    if search_algorithm == 'astar':
        path, visited = a_star_search(grid_map, start_position, goal_positions) 
    elif search_algorithm == 'bfs':
        path, visited = bfs_search(grid_map, start_position, goal_positions)
    elif search_algorithm == 'dfs':
        path, visited = dfs_search(grid_map, start_position, goal_positions)
    elif search_algorithm == 'gbfs':
        path, visited = greedy_best_first_search(grid_map, start_position, goal_positions)
    elif search_algorithm == 'iddfs':
        path, visited = iddfs_search(grid_map, start_position, goal_positions)
    elif search_algorithm == 'astar_weighted':
        while True:
            try:
                weight = float(input("Enter the weight for A* search: "))
                break  
            except ValueError:
                print("Invalid input. This is probably not something that can be convert into a float")
        path, visited = a_star_search_weighted(grid_map, start_position, goal_positions, weight)

    # Display the results
    if path:
        print(f"Path found:", path)
        with open('output.txt', 'w') as file:
            # Write the output directly to the file
            file.write(f"{path}")
        
        movements = interpret_movements(path)
        print("Path Interpretation:")
        for i, movement in enumerate(movements, start=1):
            print(f"Step {i}: {movement}")
        
        total_nodes_visited = count_nodes_visited(visited)
        print(f"Total nodes visited: {total_nodes_visited}")

        for position in path:
            grid_map[position[1]][position[0]] = 'P'
        draw_map(grid_map, start_position, goal_positions, obstacles, path, visited)
    else:
        print(f"No path found using {search_algorithm}.")

if __name__ == "__main__":
    main()













