# PA2 - Mazeworld
## Readme
### by Ariel Attias, for COSC 76 21F

Now that the file is unzipped, run `test_mazeworld.py` to see how A* finds multi-robot paths in the test mazes.
Run `test_sensorless.py` to see how A* narrows down belief states to localize a robot in a maze.

To run your own test, create a maze in a `filename.maz` file. 

1. Running a mazeworld test:

The maze should have between 1-3 robots.

 a. Call maze with `testmazeX = Maze("filename.maz")`
 b. Pass maze into a problem like `test_mp = MazeworldProblem(test_maze3, (x1, y1, x2, y2,... xN, yN))`    where N is the number of robots in the maze
 c. Lastly, animate the path with a statment similar to `print(astar_search(test_mp2, test_mp2.heuristic_fn))`
 
2. 
