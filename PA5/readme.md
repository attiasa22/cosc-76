### PA5 - ReadMe
#### COSC 76
##### Ariel Attias

Installation: Unzip the files into your preferred location on your computer.
 
 Execution: Run `python3 PATH/TO/solve_sudoku.py PATH/TO/test_case.cnf` to generate the sudoku board representation for the clauses in the file run.
 
 To experiment with heuristics and search strategies:

A. Search Strategy

1. WalkSat: Is the default. `result` in `solve_sudoku.py` references `sat.walksat()` on line 15.
2. Gsat: To set gsat, modify line 15 in `solve_sudoku.py` to `result = sat.gsat(max_flips, max_tries)`

B. Heuristics

1. Max Flips and Max tries can be modified for gsat when declared, and directly in the function for walksat.
2. h , the probability barrier to choose a random variable to flip or to flip given the count, can be modified in the function. 
