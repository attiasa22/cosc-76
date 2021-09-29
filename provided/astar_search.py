from SearchSolution import SearchSolution
from heapq import heappush, heappop
import Maze, MazeworldProblem

class AstarNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

    def __init__(self, state, heuristic, parent=None, transition_cost=0,cost=0):
        # you write this part
        self.state=state
        self.heuristic=heuristic
        self.parent=parent
        self.transition_cost=transition_cost
        self.cost=cost

    def priority(self):
        # you write this part
        if self.parent is not None:
            return self.heuristic+self.transition_cost+self.parent.cost
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
        if search_problem.goal_test(node.state):
            print(search_problem.animate_path(backchain(node)))
            return backchain(node)
        
        for childState in search_problem.get_successors(node.state):
            # Python is finicky with using lists/tuples as dictionary keys, so i added this line
            immutableState = tuple(childState)
            transitionCost= int(not (tuple(childState[1:])==tuple(node.state[1:])))
            child_node = AstarNode(immutableState, parent= node, heuristic=heuristic_fn(childState),transition_cost=transitionCost,cost = transitionCost+node.cost )
            
            if child_node.state not in visited_cost or child_node.priority() < visited_cost[child_node.state]:
                heappush(pqueue, child_node)
                visited_cost[child_node.state] = child_node.priority()
                
    return backchain(node)
