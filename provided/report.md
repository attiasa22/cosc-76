# PA2 - Mazeworld
## Report
### by Ariel Attias for COSC 76 21F

**(a) Description: How do your implemented algorithms work? What design decisions did you make? How you laid out the problems?**

1. `MazeworldProblem`
  A MazeworldProblem class instance is used to solve a specific problem. I defined a robotCount, a start state, and a goal state in addition to the maze to help solve the problem. 
  I defined the `get_successors(self, state)`, `check_successors(self, state, xCoordinate, yCoordinate)`, `goal_test(self, locations)`, `calculatetransitioncost(self, childState, node)`, and the `heuristic_fn(self, state)` to help solve the problem.
  
  `get_successors(self, state)` creates new successor states for all possible actions: the robot moves up, down, left, or right, or waits their turn.
  This is done by finding the coordinates, defines as the (2 * robot number + 1, 2 * robot number + 1). We count the robots starting from zero, and store the coordinates for all the robots in the same list.
  Each state is checked to be permissible by `check_successors(self, state, xCoordinate, yCoordinate)`. If  the new location is a floor and does not already contain a robot, the action is allowed and the new state is added to the list of successor states.
  `calculatetransitioncost(self, childState, node)`, gives a cost of 1 if the robot has moved, and 0 otherwise, and the `heuristic_fn(self, state)` gives a score based on each robots manhattan distance to their respective goal locations.
  `goal_test(self, locations)` returns true if the current locations of the robots match the goal locations defined at the beginning of the problem.
  
2. `SensorlessProblem`
A SensorlessProblem class instance is used to solve the blind robot problem for 1 robot. Only the stat state and maze are initialized by the constructor. The start state is every open tile in the maze, which is found by `initbeliefstates`, which loops through the cells in the maze. Once we have the start state, the problem can be modelled as a search problem solved by A*.

`get_successors(self, belief_states)` returns the belief states arising from the four possible directions. For each direction, it calls `check_successors(self, x_change, y_change, belief_states)`. This function checks if each of the belief states leads to a new belief state, or if the old belief state remains.
`calculatetransitioncost(self, childState, node)`, gives a cost of 1, and the `heuristic_fn(self, state)` gives a score based on the number of remaining belief states.

Both heuristics are consistent and lead to A* being optimal, as confirmed by comparing the results of this heuristic with the null heuristic.

3. `AstarNode` packs the state, its heuristic, its parent node, and the cost up to and including that node. It also includes the `priority()` and `__lt__(self, other)` for the heap. The first function returns the sum of the heuristic and the cost of the node, and the latter is a comparator for the heap.

4. A* follows the pseudocode for the algorithm closely, and additionally implements the priority queue with the methods found at https://docs.python.org/3/library/heapq.html#priority-queue-implementation-notes to solve the issues related to sorting stability, tuple comparisons, priority changes, and the need to delete pending states. The search solution class is then used to store the length of the final path, as well as the associated cost.

**(b) Evaluation: Do your implemented algorithms actually work? How well? If it doesn’t work, can you tell why not? What partial successes did you have that deserve partial credit?**

My implemented algorithms work well, as confirmed by their integration with the other classes and the animated path function. The heuristics were double checked with the null heuristic to ensure optimality of A*. The implementation of the priority queue following the Python documentation also helps with runtime and the optimailty of the priority queue, which is needed for A*.

**(c) Responses to discussion questions that are included within the points in "Required tasks", marked as Discussion questions.**

Mazeworld

**If there are k robots, how would you represent the state of the system? Hint -- how many numbers are needed to exactly reconstruct the locations of all the robots, if we somehow forgot where all of the robots were? Further hint. Do you need to know anything else to determine exactly what actions are available from this state?**

  For k robots, the state of the system can be represented as (r, x_1,y_2,..., x_k,y_k), so we need 2k numbers to determine the locations, and 1 number, r, to designate which robot's turn it is. 

**Give an upper bound on the number of states in the system, in terms of n and k.**

  A rough upper bound leads to k robots, n possible numbers for x_1, y_2... or O(k(n^(2k)))

**Give a rough estimate on how many of these states represent collisions if the number of wall squares is w, and n is much larger than k.**

  If there are w wall squares, the ratio of walls to total cells is (w/(n^2)) which leads to O(w(n^(2k-2))) states with collisions on walls (ignoring robots on the same cell).

**If there are not many walls, n is large (say 100x100), and several  robots (say 10), do you expect a straightforward breadth-first search on the state space to be computationally feasible for all start and goal pairs? Why or why not?**

No, as there would be around O(k(n^(2k)))= O(10(100^20)) possible states, which would be very computationally difficult to explore with BFS.

**Describe a useful, monotonic heuristic function for this search space. Show that your heuristic is monotonic. See the textbook for a formal definition of monotonic.**

  A usefule monotonic heuristic function for this search space is the manhattan distance of each robot to its goal location. A heuristic is monotone if h(n)<= h(n')+cost(n->n'). The manhattan can only increase or decrease by one at a time, since the cost is also 1, two adjacent cells, A, B, with B closer to the goal node, leads to the inequality h(A)<= h(B)+cost(A->B) , h(A)<= h(B)+1, h(A)<= h(A)-1+1 ,  h(A)<= h(A), which is true. Since the function is monotone for adjacent cells, since the costs are the same and additive for the distance of the cells and the manhattan distance at most changes by 1 for adjacent tiles, the manhattan distance must be a monotonic heuristic.

**It may seem that you can just plan paths for the robots independently using three different breadth-first-searches, but this approach won't work very well if the robots get close to one another or have to move around one another. Therefore, you should plan paths in the complete state space for the system.**

**Describe why the 8-puzzle in the book is a special case of this problem. Is the heuristic function you chose a good one for the 8-puzzle?
The state space of the 8-puzzle is made of two disjoint sets.  Describe how you would modify your program to prove this. (You do not have to implement this.)**

  The 8 puzzle problem is a special case of this general idea, as the tiles are always adjacent to at least two other tiles, and the tiles (except for 1), are all situated in another tile's goal location, and a tile is in its goal location. The manhattan distance is an admissible heuristic as it is monotonic and must underestimate the real cost, but perhaps it does not approach the best function value, which would be nearer to the real cost of a state's path.

To show this, I would create the 8-tile "maze" with the 8 robots and try to use Mazeworld problem to solve it for some number of goal states, with the start state being the "solution" (e.g. tiles are numbered in order). Inverting two of the tiles should create a new board that is unreachable by A* from the start state.

Blindrobot

**Describe what heuristic you used for the A* search. Is the heuristic optimistic? Are there other heuristics you might use? (An excellent might compare a few different heuristics for effectiveness and make an argument about optimality.)**

For the blindrobot A* search, I used the number of robots still present as a heuristic. The heuristic is optimistic.
Other heuristics you might use include the euclidean or manhattan distance between the farthest two belief states (or more than 2, etc). Another heuristic might be to find the change in belief states from the previous state.
