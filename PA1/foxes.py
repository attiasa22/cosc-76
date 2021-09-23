from FoxProblem import FoxProblem
from uninformed_search import bfs_search, dfs_search, ids_search
import timeit
# Create a few test problems:
problem331 = FoxProblem((3, 3, 1))
problem541 = FoxProblem((5, 4, 1))
problem551 = FoxProblem((5, 5, 1))

# Run the searches.
#  Each of the search algorithms should return a SearchSolution object,
#  even if the goal was not found. If goal not found, len() of the path
#  in the solution object should be 0.

print(bfs_search(problem331))
print(dfs_search(problem331))
print(ids_search(problem331))

print(bfs_search(problem551))
print(dfs_search(problem551))
print(ids_search(problem551))

print(bfs_search(problem541))
print(dfs_search(problem541))
print(ids_search(problem541))
'''
print("331")
print(timeit.timeit('bfs_search(FoxProblem((3, 3, 1)))', 'from uninformed_search import bfs_search ; from FoxProblem import FoxProblem',number=100))
print(timeit.timeit('dfs_search(FoxProblem((3, 3, 1)))', 'from uninformed_search import dfs_search ; from FoxProblem import FoxProblem',number=100))
print(timeit.timeit('ids_search(FoxProblem((3, 3, 1)))', 'from uninformed_search import ids_search ; from FoxProblem import FoxProblem',number=100))
print("551")
print(timeit.timeit('bfs_search(FoxProblem((5, 5, 1)))', 'from uninformed_search import bfs_search ; from FoxProblem import FoxProblem',number=100))
print(timeit.timeit('dfs_search(FoxProblem((5, 5, 1)))', 'from uninformed_search import dfs_search ; from FoxProblem import FoxProblem',number=100))
print(timeit.timeit('ids_search(FoxProblem((5, 5, 1)))', 'from uninformed_search import ids_search ; from FoxProblem import FoxProblem',number=100))
print("541")
print(timeit.timeit('bfs_search(FoxProblem((5, 4, 1)))', 'from uninformed_search import bfs_search ; from FoxProblem import FoxProblem',number=100))
print(timeit.timeit('dfs_search(FoxProblem((5, 4, 1)))', 'from uninformed_search import dfs_search ; from FoxProblem import FoxProblem',number=100))
print(timeit.timeit('ids_search(FoxProblem((5, 4, 1)))', 'from uninformed_search import ids_search ; from FoxProblem import FoxProblem',number=100))
'''