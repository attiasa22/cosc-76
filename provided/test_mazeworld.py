from MazeworldProblem import MazeworldProblem
from Maze import Maze

#from uninformed_search import bfs_search
from astar_search import astar_search

# null heuristic, useful for testing astar search without heuristic (uniform cost search).
def null_heuristic(state):
    return 0

# Test problems
test_maze3 = Maze("maze3.maz")
test_maze4 = Maze("maze4.maz")
test_maze5 = Maze("maze5.maz")
test_maze6 = Maze("maze6.maz")
test_maze7 = Maze("maze7.maz")
test_maze8 = Maze("maze8.maz")
test_maze9 = Maze("maze9.maz")

test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))
test_mp2 = MazeworldProblem(test_maze4, ( 1, 2, 1, 1, 1, 0))
test_mp3 = MazeworldProblem(test_maze5, ( 8, 9, 7, 9, 6, 9))
test_mp4 = MazeworldProblem(test_maze6, ( 8, 8, 8, 1, 1, 8))
test_mp5 = MazeworldProblem(test_maze7, ( 1, 9, 1, 1, 1, 4))
test_mp6 = MazeworldProblem(test_maze8, ( 8, 1, 8, 8, 1, 1))

print(test_mp.get_successors(test_mp.start_state))

#this should explore a lot of nodes; it's just uniform-cost search
result = astar_search(test_mp, null_heuristic)
print(result)

# this should do a bit better:
result = astar_search(test_mp, test_mp.heuristic_fn)
print(result)
test_mp.animate_path(result)

# Your additional tests here:
result=astar_search(test_mp2, test_mp2.heuristic_fn) # works in under 1 minute
print(result)
test_mp2.animate_path(result)

result=astar_search(test_mp3, test_mp3.heuristic_fn) # works in under 1 minute
print(result)
test_mp3.animate_path(result)

result=astar_search(test_mp4, test_mp4.heuristic_fn)
print(result)
test_mp4.animate_path(result)

result = astar_search(test_mp5, test_mp5.heuristic_fn)# works
print(result)
test_mp5.animate_path(result)

result = astar_search(test_mp6, test_mp6.heuristic_fn) # works in under 1 minute
print(result)
test_mp6.animate_path(result)
