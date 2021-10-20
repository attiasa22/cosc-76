from SearchProblem import SearchProblem
from MapColoring import MapColoring
from CircuitBoardFitting import CircuitBoardFitting
from CircuitBoardFitting2 import CircuitBoardFitting2

australia = {"WA": ["NT","SA"], 
             "NT": ["WA","SA","Q"],
             "SA": ["WA","NT","Q", "NSW"],
             "Q": ["NT","SA", "NSW"], 
             "NSW": ["SA","Q", "V"],
             "V": ["SA", "NSW"],
              "T": []
             }

easy = {"1": ["2","3","4"], 
        "2": ["1","3","4"],
        "3": ["1","2"],
        "4": ["1","2",]
             }

map1 = MapColoring(australia, 3)
map2 = MapColoring(easy, 3)

#print(SearchProblem(search_problem = map1).backtracking_search())
#print(SearchProblem(search_problem = map1, variable_heuristic = "mrv").backtracking_search())
#print(SearchProblem(search_problem = map1, variable_heuristic = "degree_heuristic").backtracking_search())
#print(SearchProblem(search_problem = map1,value_heuristic="lcv").backtracking_search())
#print(SearchProblem(search_problem = map1, should_inference = True).backtracking_search())
#print(SearchProblem(search_problem = map2, should_inference = True).backtracking_search())

chips ={"a": [2,3],
        "b": [2,5],
        "c": [3,2],
        "e": [1,7]}

#circuit_board = CircuitBoardFitting(3,10,chips)
circuit_board2 = CircuitBoardFitting2(3,10,chips)
print(SearchProblem(search_problem = circuit_board2).backtracking_search())
circuit_board2.draw_board()