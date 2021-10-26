# COSC 76 - PA4
# Ariel Attias

from SearchProblem import SearchProblem
from MapColoring import MapColoring
from CircuitBoardFitting import CircuitBoardFitting

# Map Coloring problems take in a constraint graph as a dictionary - the list contain's the key's neighbors
australia = {"WA": ["NT","SA"], 
             "NT": ["WA","SA","Q"],
             "SA": ["WA","NT","Q", "NSW"],
             "Q": ["NT","SA", "NSW"], 
             "NSW": ["SA","Q", "V"],
             "V": ["SA", "NSW"],
              "T": []
             }
# simpler map for debugging
easy = {"1": ["2","3","4"], 
        "2": ["1","3","4"],
        "3": ["1","2"],
        "4": ["1","2",]
             }

map1 = MapColoring(australia, 3)
map2 = MapColoring(easy, 3)

#Run these one at a time

#print(SearchProblem(search_problem = map1).backtracking_search())
#print(SearchProblem(search_problem = map1, variable_heuristic = "mrv").backtracking_search())
#print(SearchProblem(search_problem = map1, variable_heuristic = "degree_heuristic").backtracking_search())
#print(SearchProblem(search_problem = map1,value_heuristic="lcv").backtracking_search())
print(SearchProblem(search_problem = map1, variable_heuristic = "degree_heuristic", value_heuristic="lcv", should_inference = True).backtracking_search())

#print(SearchProblem(search_problem = map2, should_inference = True).backtracking_search())

# List of chips for the circuit board problem 
#Keys are chip names and list are the height and width of that chip
chips ={"a": [2,3],
        "b": [2,5],
        "c": [3,2],
        "e": [1,7]}

#Create a circuit board with the chips and the heigh and width of the board
circuit_board = CircuitBoardFitting(3,10,chips)

#print(SearchProblem(search_problem = circuit_board, variable_heuristic = "degree_heuristic").backtracking_search())
print(SearchProblem(search_problem = circuit_board, variable_heuristic = "degree_heuristic", value_heuristic="lcv", should_inference = True).backtracking_search())

#After solving the circuit board problem, print out the solution with draw_board()
circuit_board.draw_board()
