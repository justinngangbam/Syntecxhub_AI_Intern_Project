import heapq

# 1. Define the Node class to keep track of positions and costs
class Node:
    def __init__(self, position, parent=None):
        self.position = position  # (row, col)
        self.parent = parent
        self.g = 0  # Cost from start to current node
        self.h = 0  # Estimated cost from current node to goal
        self.f = 0  # Total cost (g + h)
        
    # Allows the priority queue to compare nodes based on their 'f' cost
    def __lt__(self, other):
        return self.f < other.f

# 2. Define the heuristic function (Manhattan Distance)
def heuristic(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

# 3. Implement the A* Algorithm
def astar(maze, start, goal):
    start_node = Node(start)
    goal_node = Node(goal)
    
    open_list = []
    closed_set = set()
    
    # Add start node to the open list
    heapq.heappush(open_list, (start_node.f, start_node))
    
    # Directions: Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while open_list:
        # Get the node with the lowest f cost
        current_node = heapq.heappop(open_list)[1]
        
        # If we reached the goal, trace backward to get the path
        if current_node.position == goal_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1] # Reverse it so it goes from start to goal
            
        closed_set.add(current_node.position)
        
        # Check adjacent neighbors
        for direction in directions:
            node_position = (current_node.position[0] + direction[0], current_node.position[1] + direction[1])
            
            # Make sure the neighbor is within the maze grid
            if (node_position[0] > (len(maze) - 1) or node_position[0] < 0 or 
                node_position[1] > (len(maze[0]) - 1) or node_position[1] < 0):
                continue
                
            # Make sure the terrain is walkable (0 = path, 1 = wall)
            if maze[node_position[0]][node_position[1]] != 0:
                continue
                
            # Skip if already visited
            if node_position in closed_set:
                continue
                
            # Create new node for this neighbor
            neighbor = Node(node_position, current_node)
            neighbor.g = current_node.g + 1
            neighbor.h = heuristic(neighbor.position, goal_node.position)
            neighbor.f = neighbor.g + neighbor.h
            
            # Add to open list to be explored
            heapq.heappush(open_list, (neighbor.f, neighbor))
            
    return None # Return None if no path exists

# 4. Visualization Function
def visualize_maze(maze, path, start, goal):
    if not path:
        print("No valid path found!")
        return

    # Create a visual copy of the maze
    maze_vis = [row[:] for row in maze]
    
    # Mark the path with '*'
    for (r, c) in path:
        if (r, c) != start and (r, c) != goal:
            maze_vis[r][c] = '*'
            
    # Mark start and goal
    maze_vis[start[0]][start[1]] = 'S'
    maze_vis[goal[0]][goal[1]] = 'G'
    
    print("\nMaze Solution:")
    for row in maze_vis:
        # Print walls as '█' and empty spaces normally
        print(" ".join(str(cell) if cell != 1 else '█' for cell in row))
    
    print(f"\nPath coordinates: {path}")

# 5. Run the code
if __name__ == '__main__':
    # 0 is a walkable path, 1 is a wall
    maze = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    
    start_pt = (0, 0)
    goal_pt = (4, 4)
    
    print("Calculating path...")
    found_path = astar(maze, start_pt, goal_pt)
    visualize_maze(maze, found_path, start_pt, goal_pt)