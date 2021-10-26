# PA4 - Report
## COSC 76 - 21F
### Ariel Attias


**(a) Description: How do your implemented algorithms work? What design decisions did you make? How you laid out the problems?**

For code clarity, I split my code into the the following classes and/or files: 

`test_constraint_problem.py` is the high level access point for users  interacting or running the code on a Map Coloring or Circuit Board problem of interest. It uses the `MapColoring`, `SearchProblem`, and `CircuitBoardFitting` classes to solve problems the user has created. Here, the user also decides if they would like to solve the csp with heuristics and/or inferencing. Please read `readme.md` for more details on how to run the software.

`MapColoring.py` takes in a map as a constraint graph and the number of colors the users would like to use. This csp is solved with the variables being the locations and the values represent the colors. For ease of solving, *n* colors are represented as numbers 1 through *n*. All the Map Coloring class needs to do to ensure that the general CSP solver can solve the Map Coloring problem is have its own constraint check and set up the domain. The constraint check verifies that neighbors do not share a color.

`CircuitBoardFitting` takes in a set of chips as variables and the size of the circuit board. THe values are created as each coordinate on the board, and the initial domains are created by checking if each chip's lower left corner can be placed at the coordinate. The constraint check verifies that two chips do not overlap. The class also has a board drawing function so that the final assignment can be displayed in ASCII art.

`SearchProblem` implements the backtracking algorithm for solving CSPs. The heuristics and inferencing are implemented following the pseudocode as well, and are abstracted away in other files, namely `heuristics.py` and `inferences.py`. In addition to following the pseudocode, additional lists were kept to keep track of the changes to domains and assignments during inferencing.

**(b) Evaluation: Do your implemented algorithms actually work? How well? If it doesn’t work, can you tell why not? What partial successes did you have that deserve partial credit? Include a comparison of running time results using different heuristics and inference.**

My algorithms work well, and follow the pseudocode very closely. This chart summarizes the number of times the algorithm backtracked with the relevant heuristics

| Problem      | No Heuristics | MRV    | LCV      | Degree Heuristic | Inferencing    | Degree Heuristic & Inferencing    |
| :---        |    :----:   |    :----:   |    :----:   | :----:   |  :----:   |          ---: |
| Map Coloring      | 7       | 7   | 7       | 7   | 4   | 3   |
| Circuit Board   | 4        | 4      | 4   | 4        | 4      | 4|

Without inferencing, since No heuristics are needed to already achieve the minimum possible number of backtracks (the number of variables), the heuristic functions are not very helpful. However, inferencing is very helpful for the Map coloring problem, as only 4 regions are visited before a solution is found.

The circuit board assignment is always </br>
`eeeeeee.cc` </br>
`aaabbbbbcc` </br>
`aaabbbbbcc`

While the map assignment for Australia is somethling like `{'NSW': 1, 'NT': 1, 'Q': 2, 'SA': 3, 'T': 1, 'V': 2, 'WA': 2}` or `{'SA': 1, 'NSW': 2, 'NT': 2, 'Q': 3, 'V': 3, 'WA': 3, 'T': 1}`.


**(c) Responses to discussion questions that are included within the points in "Required tasks".**

**(map coloring test) Describe the results from the test of your solver with and without heuristic, and with and without inference on the map coloring problem.** 

The map coloring problem was easily solved in the least possible number of backtracks without any heuristics, meaning that the heuristics also provided the smallest number possible, as seen in the chart, but thatno improvements were made.

However, inferencing produced great improvement, going from 7 backtracks needed to 4. This makes a lot of sense, as in the Australia map, knowing two bordering provinces' values will also give the value of the province itself. However, some backtracking is still required due to Tasmania being completely isolated, and the fact that all provinces have the same initial domain, leading to some ambiguity early on in the problem.

**(circuit-board) In your write-up, describe the domain of a variable corresponding to a component of width w and height h, on a circuit board of width n and height m.  Make sure the component fits completely on the board.**

Assuming that w and h are both smaller than n and m, respectively, the domain of this chip would be all the places were the lower left corner can be while the component completely fits. The size of the chips domain, D, can be described as 

|D| = (n-w+1) x (m-h+1)

For example, a 2x3 piece on a 10x10 board can fit 

|D| = (10-2+1) x (10-3+1) = 9 x 8 = 72 

72 unique ways on the board.

**(circuit-board) Consider components a and b above, on a 10x3 board.  In your write-up, write the constraint that enforces the fact that the two components may not overlap.  Write out legal pairs of locations explicitly.**

a - 3x2 \
b - 5x2 

Given the left, right, bottom, and top edges of both chips, we enforce the non-overlapping condition like so

    if not (left_x2>=right_x or left_x>=right_x2 or bottom_y2>=top_y or bottom_y>=top_y2):
    
                                overlaps = True
In english if the left edge of a box is not to the right of the right edge of the other, or vice versa, or the bottom edge of a box is not above the top of the other box, or vice versa, they must be overlapping.

For boxes a and b on board 10x3, this leads to the following pairs of locations for the lower left corner of each chip.


| a   |       b | 
| :---|     ---:|
| (0,0) or (0,1)| (3,0) or (4,0) or (5,0) or (3,1) or (4,1) or (5,1)| 
| (1,0) or (1,1)| (4,0) or (5,0) or (4,1) or (5,1)        |
| (2,0) or (2,1)| (5,0) or (5,1)       | 
| (3,0) or (3,1)| NONE        |
| (4,0) or (4,1)| NONE       | 
| (5,0) or (5,1)| (0,0) or (0,1)|
| (6,0) or (6,1)| (0,0) or (1,0) or (0,1) or (1,1)| 
| (7,0) or (7,1)| (0,0) or (1,0) or (2,0) or (0,1) or (1,1) or (2,1)|


**(circuit-board) Describe how your code converts constraints, etc, to integer values for use by the generic CSP solver.**

For sake of clarity and generality, the constraints are completely abstracted away as a calculation done by the Circuit Board class, and the math only leads to a boolean from the perspective of the CSP.

Within the constraint function, the location of the lower left corner and the chip size are converted to edge locations, which can then be compared to each other.

With Python and the implementation of the dictionary, there is no need to convert variables (chip names or province names), to integers. 

Values, which are tuples representing coordinates, can also be kept as they are.