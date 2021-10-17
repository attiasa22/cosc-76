from SearchProblem import SearchProblem
from MapColoring import MapColoring

australia = {"WA": ["NT","SA"], 
             "NT": ["WA","SA","Q"],
             "SA": ["WA","NT","Q", "NSW"],
             "Q": ["NT","SA", "NSW"], 
             "NSW": ["SA","Q", "V"],
             "V": ["SA", "NSW"],
              "T": []
             }

map1 = MapColoring(australia, 3)
print(SearchProblem(search_problem = map1).backtracking_search())