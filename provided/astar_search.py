from SearchSolution import SearchSolution
from heapq import heappush, heappop
import Maze, MazeworldProblem

class AstarNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

    def __init__(self, state, heuristic, parent=None, transition_cost=0):
        # you write this part
        self.state=state
        self.heuristic=heuristic
        self.parent=parent
        self.transition_cost=transition_cost

    def priority(self):
        # you write this part
        return self.heuristic+self.transition_cost

    # comparison operator,
    # needed for heappush and heappop to work with AstarNodes:
    def __lt__(self, other):
        return self.priority() < other.priority()


# take the current node, and follow its parents back
#  as far as possible. Grab the states from the nodes,
#  and reverse the resulting list of states.
def backchain(node):
    result = []
    current = node
    while current:
        result.append(current.state)
        current = current.parent

    result.reverse()
    return result

def astar_search(search_problem, heuristic_fn):
    # I'll get you started:
    start_node = AstarNode(search_problem.start_state, heuristic_fn(search_problem.start_state))
    pqueue = []
    heappush(pqueue, start_node)

    solution = SearchSolution(search_problem, "Astar with heuristic " + heuristic_fn.__name__)

    visited_cost = {}
    visited_cost[start_node.state] = 0

    # you write the rest:
    while len(pqueue):
        node = heappop(pqueue)
        if search_problem.goal_test(node.state[1:]):
            print(search_problem.animate_path(backchain(node)))
            return backchain(node)
        
        for childState in search_problem.get_successors(node.state):
            # Python is finicky with using lists/tuples as dictionary keys, so i added this line
            immutableState = tuple(childState)

            child_node = AstarNode(immutableState, parent= node, heuristic=heuristic_fn(childState),transition_cost=1)
            
            
            if child_node.state not in visited_cost or child_node.priority() < visited_cost[child_node.state]:
                heappush(pqueue, child_node)
                #print(search_problem.animate_path(backchain(child_node))) 
                visited_cost[child_node.state] = child_node.priority()

    return []

if __name__ == "__main__":
    test_maze3 = Maze.Maze("maze3.maz")
    test_mp = MazeworldProblem.MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))
    '''
    ##.##
    #...#
    #.#.#
    #...#
    #...#
    #.###
    \robot 1 0
    \robot 1 1
    \robot 2 1
    '''
    print(astar_search(test_mp, test_mp.heuristic_fn))