from display import display_sudoku_solution
import random, sys
from SAT import SAT

if __name__ == "__main__":
    # for testing, always initialize the pseudorandom number generator to output the same sequence
    #  of values:
    random.seed(1)

    puzzle_name = str(sys.argv[1][:-4])
    sol_filename = puzzle_name + ".sol"

    sat = SAT(sys.argv[1])
    #display_sudoku_solution("PA5/rows_and_cols.sol")
    #result = sat.walksat()
    result = sat.gsat(30000,10)
    
    if result:
        sat.write_solution(sol_filename)

        display_sudoku_solution(sol_filename)