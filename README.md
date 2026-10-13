Maze Solver Using A* Search:

Developed as part of the AI Internship at Syntecxhub, this project implements an intelligent pathfinding algorithm to navigate a 2D grid environment. The program evaluates coordinate data to identify the shortest, most optimal route from a starting position to a designated goal while avoiding predefined obstacles.

Core Features:

1. Grid Node Representation: Models the maze environment as a coordinate-based grid where each cell acts as a distinct node with specific traversal properties         (e.g., 0 for an open path, 1 for a wall).

2. A Search Implementation:* Utilizes priority queue structures to dynamically evaluate and explore the most promising paths first.

3. Manhattan Distance Heuristic: Calculates the estimated cost from the current node to the goal, restricting movement to four primary directions (up, down, left, right) to prevent distance underestimation and optimize the search speed.

4. Exception Handling: Automatically detects and manages unreachable cases, halting the search and returning a clear status message if the goal is completely          enclosed by walls.

5. Console Visualization: Overlays the final reconstructed path directly onto a visual grid in the terminal using distinct characters (such as * for the path, S       for Start, and G for Goal) to instantly verify the logic.

How It Works:

1. The algorithm evaluates routes using the core A* pathfinding formula: $f(n) = g(n) + h(n)$.

2. Initialize: The starting node is placed into an "open list" (a priority queue) to begin the evaluation process

3. Evaluate Costs: The engine continuously selects the node with the lowest total cost, or $f(n)$. This total combines the exact distance traveled from the          start, $g(n)$, with the educated heuristic guess of the remaining distance to the goal, $h(n)$.

4. Explore Neighbors: It checks all valid adjacent nodes (ignoring walls, out-of-bounds coordinates, and fully explored nodes in the "closed set"). It calculates    their costs and records their "parent" node to remember the exact step-by-step journey.

5. Reconstruct Path: Once the target node is found, the system traces the sequence of stored parent nodes backward to the start, generating the final sequential     path.

Execution:

To run the solver locally, open your terminal in the project directory and execute the Python script: python astar_solver.py
