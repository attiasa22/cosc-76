# PA2 - MAzeworld
## Report
### by Ariel Attias for COSC 76 21F



A short typewritten report describing your results. The report should contain three main sections:
(a) Description: How do your implemented algorithms work? What design decisions did you make? How you laid out the problems?

1. `MazeworldProblem`
  A MazeworldProblem class instance is used to solve a specific problem. I defined a robotCount, a start state, and kept the height and width of the maze defined in the constructor. 
  I defined the `get_successors(self, state)`, `check_successors(self, state, xCoordinate, yCoordinate)`, `goal_test(self, locations)`, and the `heuristic_fn(self, state)` to help solve the problem.
  
  `get_successors(self, state)` creates new successor states for all possible actions: the robot moves up, down, left, or right, or waits their turn.
  This is done by finding the coordinates, defines as the (2 * robot number + 1, 2 * robot number + 1). We count the robots starting from zero, and store the coordinates for all the robots in the same list.
  Each state is checked to be permissible by `check_successors(self, state, xCoordinate, yCoordinate)`. If  the new location is a floor and does not already contain a robot, the action is allowed and the new state is added to the list of successor states.
  `goal_test(self, locations)` returns true if the current locations of the robots match the goal locations defined at the beginning of the problem.
  
  
  
2. `SensorlessProblem`

(b) Evaluation: Do your implemented algorithms actually work? How well? If it doesn’t work, can you tell why not? What partial successes did you have that deserve partial credit? 
(c) Responses to discussion questions that are included within the points in "Required tasks", marked as Discussion questions.
