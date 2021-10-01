# You write this:
from SensorlessProblem import SensorlessProblem
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

test_mp = SensorlessProblem(test_maze3)
test_mp = SensorlessProblem(test_maze3)
test_mp2 = SensorlessProblem(test_maze4)
test_mp3 = SensorlessProblem(test_maze5)
test_mp4 = SensorlessProblem(test_maze6)
test_mp5 = SensorlessProblem(test_maze7)
test_mp6 = SensorlessProblem(test_maze8)
test_mp7 = SensorlessProblem(test_maze9)
 

print(test_mp.get_successors(test_mp.start_state))

# this should explore a lot of nodes; it's just uniform-cost search
#result = astar_search(test_mp, null_heuristic)
#print(result)

# this should do a bit better:
result = astar_search(test_mp, test_mp.heuristic_fn)
print(result)
test_mp.animate_path(result)

# Your additional tests here:
#print(astar_search(test_mp2, test_mp2.heuristic_fn))# works in under 1 minute
#print(astar_search(test_mp3, test_mp3.heuristic_fn)) # works in under 1 minute
#print(astar_search(test_mp4, test_mp4.heuristic_fn)) # works in 2-3 minutes
#print(astar_search(test_mp5, test_mp5.heuristic_fn)) # works
#print(astar_search(test_mp6, test_mp6.heuristic_fn)) # works in under 1 minute
#print(astar_search(test_mp7, test_mp6.heuristic_fn)) # works in under 1 minute