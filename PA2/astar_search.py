from SearchSolution import SearchSolution
from heapq import heappush, heappop
import itertools

class AstarNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

    def __init__(self, state, heuristic, parent=None,cost=0):
        # you write this part
        self.state = state
        self.heuristic = heuristic
        self.parent = parent
        self.cost = cost

    def priority(self):
        # you write this part
        return self.heuristic + self.cost

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
    heappush(pqueue, [0,0,start_node])

    solution = SearchSolution(search_problem, 'Astar with heuristic ' + heuristic_fn.__name__)

    visited_cost = {}
    visited_cost[start_node.state] = 0

    # you write the rest:
    # the following is adapted from python documentation to deal with repeat states
    counter = itertools.count()
    REMOVED = '<removed-task>'
    entry_finder = {}
    entry_finder[start_node.state] = [0,0,start_node]

    def add_task(task, priority = 0):
        'Add a new task or update the priority of an existing task'
        if task.state in entry_finder:
            remove_task(task)
        count = next(counter)
        entry = [priority, count, task]
        entry_finder[task.state] = entry
        heappush(pqueue, entry)

    def remove_task(task):
        'Mark an existing task as REMOVED.'
        entry = entry_finder.pop(task.state)
        entry[-1] = REMOVED

    def pop_task():
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while pqueue:
            priority, count, task = heappop(pqueue)
            if task is not REMOVED:
                del entry_finder[task.state]
                return task
        raise KeyError('pop from an empty priority queue')   

    while len(pqueue):

        node = pop_task()
 
        if search_problem.goal_test(node.state):
            solution.path=backchain(node)
            solution.cost=node.cost
            solution.nodes_visited=len(solution.path)

            print("COST: %d" %solution.cost)
            print("NODES VISITED: %d" %solution.nodes_visited)

            return solution.path
        for childState in search_problem.get_successors(node.state):
            
            transition_cost = search_problem.calculatetransitioncost(childState, node)
            new_cost = transition_cost+node.cost
            child_node = AstarNode(tuple(childState), parent = node, heuristic = heuristic_fn(childState), cost = new_cost )
            
            if child_node.state not in visited_cost or child_node.cost < visited_cost[child_node.state]:
                add_task(child_node, priority = (child_node.priority()))
                visited_cost[child_node.state] = child_node.cost

    return backchain(node)
