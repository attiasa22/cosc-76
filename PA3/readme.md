### PA3 - ReadMe
#### COSC 76
##### Ariel Attias



Installation: Unzip the files into your preferred location on your computer.
 
 Execution: Run `python3 PATH/TO/test_constraint_problem.py` to generate the solutions for the Australian map coloring problem and the circuit board problem.
 
 To experiment with other start states and heuristics
 A. Map coloring
 1. Create a new graph (implemented as a dictionrary) with the provinces as keys and the list of bordering provinces as the value.
 2. Pass the graph and the maximum number of colors into a new Map Coloring instance, `map1 = MapColoring(australia, 3)`
 
 B. Circuit Board Fitting
 1. Create some chips (implemented as a dictionrary) with the chip names as keys and the list of dimensions as the value.
 2. Pass the chips and the dimensions of the circuit board into a new CircuitBoardFitting instance, `circuit_board = CircuitBoardFitting(3,10,chips)`


Pass either instance into a `SearchProblem`, and print `backtracking_search()` of that instance to see the assignment. For example, `print(SearchProblem(search_problem = map1).backtracking_search())`. 

To use heuristics, simply pass in "mrv", "degree_heuristic," or "lcv" as a `variable_heuristic`, like `print(SearchProblem(search_problem = map1, variable_heuristic = "mrv").backtracking_search())`. 

To use inferencing, declare `should_inference = True`, like `print(SearchProblem(search_problem = map1, should_inference = True).backtracking_search())`
