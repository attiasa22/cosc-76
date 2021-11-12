# PA6 - Hidden Markov Models
## Readme
### by Ariel Attias, for COSC 76 21F

Now that the file is unzipped, run `PA6/MarkovSolver.py` to see how filtering sets the probabilities for each floor in the maze to have the robot.

To run your own test, create a maze in a `filename.maz` file. 

1. Running a MazeProblem:

The maze floors should be created using one of 4 colors: ("R", "G", "B", "Y")

 a. Call maze with `testmazeX = Maze("filename.maz")` 
 
 b. Pass maze into a problem like `problem = MazeProblem(test_maze1, t_p)` where t_p is the true positive probability of the sensor.
 
 c. Create a solver instance like so: `solver = MarkovSolver(problem)`

 d.  Use the HMM with `solver.filtering(x)` where x is the number of times filtering is done.

 e. Lastly, call `problem.show_solution()` to view the model's values.
 
 ### Extra Credit
 To run the extra credit viterbi algorithm, simply uncomment the line `solver.viterbi()`