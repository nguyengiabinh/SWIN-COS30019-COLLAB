from create_and_draw_map import create_grid_map, draw_map
from astar_search import asm1_a_star_search
from bfs_search import asm1_bfs
from dfs_search import asm1_dfs  
from greedy_best_first_search import asm1_gdf_search
import os

def main():

    while True:
        file_path = input("Enter the file path: ")

        if os.path.exists(file_path):
            break
        else:
            print(f"The file '{file_path}' does not exist. Please enter a valid file path.")

    algorithms = ['a_star', 'bfs', 'dfs', 'gbfs']
    while True:
        search_algorithm = input("Enter the search algorithm ('astar', 'bfs', 'dfs', 'gbfs'): ")

        if search_algorithm in algorithms:
            print(f"Chosen search algorithm: {search_algorithm}")
            break
        else:
            print("Invalid search algorithm. Please enter a valid search algorithm.")

    grid_map, start_position, goal_positions, obstacles = create_grid_map(file_path)
    draw_map(grid_map, start_position, goal_positions, obstacles)



    if search_algorithm == 'a_star':
        path, visited = asm1_a_star_search(grid_map, start_position, goal_positions)
    elif search_algorithm == 'bfs':
        path, visited = asm1_bfs(grid_map, start_position, goal_positions[0])
    elif search_algorithm == 'dfs':
        path, visited = asm1_dfs(grid_map, start_position, goal_positions[0]) 
    elif search_algorithm == 'gbfs':
        path, visited = asm1_gdf_search(grid_map, start_position, goal_positions[0])
    else:
        raise ValueError("Invalid search algorithm. Use 'a_star', 'bfs', 'dfs', or 'greedy_best_first'.")

    if path:
        print(f"Path found using {search_algorithm}:", path)
        print(f"Visited set using {search_algorithm}:", visited)
        print("Total node visited: ", len(visited))
        for position in path:
            grid_map[position[1]][position[0]] = 'P'
        draw_map(grid_map, start_position, goal_positions, obstacles, path, visited)
    else:
            print(f"No path found using {search_algorithm}.")

if __name__ == "__main__":
    main()