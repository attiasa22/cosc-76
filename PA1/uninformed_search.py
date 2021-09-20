
from collections import deque
from SearchSolution import SearchSolution

# you might find a SearchNode class useful to wrap state objects,
#  keep track of current depth for the dfs, and point to parent nodes
class SearchNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

    def __init__(self, state, parent=None):
        # you write this part
        self.depth = 0
        self.state = state
        self.parent = parent

# you might write other helper functions, too. For example,
#  I like to separate out backchaining, and the dfs path checking functions
def bfs_search(search_problem):
    visited={}
    frontier = deque()
    startNode = SearchNode(search_problem.start_state)
    frontier.append(startNode)

    while len(frontier):
        currentNode = frontier.popleft()
        currentState = currentNode.state

        visited[''.join([str(count) for count in currentState])]=0
        
        if search_problem.goal_test(currentState):
            return backchain(currentNode)
        print("Parent:")
        print(currentState)
        print("Children:")
        print(search_problem.get_successors(currentState))
        for child in search_problem.get_successors(currentState):
            childNode = SearchNode(child,parent= currentNode)

            if ''.join([str(count) for count in childNode.state]) not in visited:
                frontier.append(childNode)


    return []

def backchain(currentNode):
    backchain = []

    while currentNode.parent is not None:
        backchain.append(currentNode.state)
        currentNode = currentNode.parent
    
    backchain.append(currentNode.state)

    return backchain
# Don't forget that your dfs function should be recursive and do path checking,
#  rather than memoizing (no visited set!) to be memory efficient

# We pass the solution along to each new recursive call to dfs_search
#  so that statistics like number of nodes visited or recursion depth
#  might be recorded
def dfs_search_iterative(search_problem, depth_limit=100, node=None, solution=None):
    # if no node object given, create a new search from starting state
    if node == None:
        node = SearchNode(search_problem.start_state)
        solution = SearchSolution(search_problem, "DFS")

    # you write this part
    frontier = deque()
    visited= set()
    startNode = SearchNode(search_problem.start_state)
    
    frontier.append(startNode)

    while len(frontier) :
        currentNode = frontier.pop()
        currentState = currentNode.state
        visited.add([''.join([str(count) for count in currentState])])
        
        if search_problem.goal_test(currentState):
            return backchain(currentNode)

        for child in search_problem.get_successors(currentState):
            childNode = SearchNode(child,parent= currentNode)
            childNode.depth = currentNode.depth+1

            if childNode.depth <= depth_limit and ''.join([str(count) for count in childNode.state]) not in visited:
                frontier.append(childNode)

    return []

visited = set()
def dfs_search(search_problem, depth_limit=100, node=None, solution=None):
    # if no node object given, create a new search from starting state
    if node == None:
        node = SearchNode(search_problem.start_state)
        solution = SearchSolution(search_problem, "DFS")
    
    if search_problem.goal_test(node.state):
            return solution+[node.state]

    # you write this part
    if node.state not in visited and node.depth<100:
        print(node.state)
        visited.add(node.state) 
        for child in search_problem.get_successors(node.state):
            childNode=SearchNode(child,parent=node)
            childNode.depth=node.depth+1
            dfs_search(search_problem, depth_limit=100, node=childNode, solution=None)
    return []

def ids_search(search_problem, depth_limit=100):
    # you write this part
    # redo dfs for each depth limit
    for i in range(depth_limit):
        solution = dfs_search(search_problem, depth_limit=i) 
        if len(solution)>0:
            return solution
    return []
