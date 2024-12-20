from create_and_draw_map import create_grid_map, draw_map
from astar_search import asm1_a_star_search
from bfs_search import asm1_bfs
from dfs_search import asm1_dfs  
from greedy_best_first_search import asm1_gdf_search
from uniform_cost_search import ucs_search
from best_first_search import best_first_search
from move_actions import get_movement_directions, get_visited_node_count
import os

def main():
    """
    Main function to execute the search algorithm based on user input.
    """
    while True:
        file_path = input("Enter the file path: ")

        if os.path.exists(file_path):
            break
        else:
            print(f"The file '{file_path}' does not exist. Please enter a valid file path.")

    while True:
        search_algorithm = input("Enter the search algorithm ('astar', 'bfs', 'dfs', 'gbfs', 'ucs', 'bestfs'): ")
        algorithms = ['astar', 'bfs', 'dfs', 'gbfs', 'ucs', 'bestfs']

        if search_algorithm in algorithms:
            print(f"Chosen search algorithm: {search_algorithm}")
            break
        else:
            print("Invalid search algorithm. Please enter a valid search algorithm.")

    grid_map, start_position, goal_positions, obstacles = create_grid_map(file_path)
    draw_map(grid_map, start_position, goal_positions, obstacles)

    if search_algorithm == 'astar':
        path, visited = asm1_a_star_search(grid_map, start_position, goal_positions)
    elif search_algorithm == 'bfs':
        path, visited = asm1_bfs(grid_map, start_position, goal_positions)
    elif search_algorithm == 'dfs':
        path, visited = asm1_dfs(grid_map, start_position, goal_positions) 
    elif search_algorithm == 'gbfs':
        path, visited = asm1_gdf_search(grid_map, start_position, goal_positions)
    elif search_algorithm == 'ucs':
        path, visited = ucs_search(grid_map, start_position, goal_positions)  
    elif search_algorithm == 'bestfs':
        path, visited = best_first_search(grid_map, start_position, goal_positions)  
    else:
        raise ValueError("Invalid search algorithm. Use 'a_star', 'bfs', 'dfs', 'bestfs', or 'greedy_best_first'.")

    if path:
        print(f"Path found using {search_algorithm}:", path)
        print(f"Visited set using {search_algorithm}:", visited)
        print("Total node visited: ", len(visited))
        
        movements = get_movement_directions(path)
        print("Path Interpretation:")
        for i, movement in enumerate(movements, start=1):
            print(f"{movement}")
        for position in path:
            grid_map[position[1]][position[0]] = 'P'
        draw_map(grid_map, start_position, goal_positions, obstacles, path, visited)
    else:
        print(f"No path found using {search_algorithm}.")

if __name__ == "__main__":
    main()
