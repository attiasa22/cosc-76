'''
Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.
For example, in this diagram, the earliest ancestor of 6 is 14, and the earliest ancestor of 15 is 2. 
         14
         |
  2      4
  |    / | \
  3   5  8  9
 / \ / \     \
15  6   7    11
Write a function that, for a given individual in our dataset, returns their earliest known ancestor -- the one at the farthest distance from the input individual. If there is more than one ancestor tied for "earliest", return any one of them. If the input individual has no parents, the function should return null (or -1).
Sample input and output:

findEarliestAncestor(parentChildPairs3, 8) => 14
findEarliestAncestor(parentChildPairs3, 7) => 14
findEarliestAncestor(parentChildPairs3, 6) => 14
findEarliestAncestor(parentChildPairs3, 15) => 2
findEarliestAncestor(parentChildPairs3, 14) => null or -1
findEarliestAncestor(parentChildPairs3, 11) => 14
Additional example:
  14
  |
  2      4    1
  |    / | \ /
  3   5  8  9
 / \ / \     \
15  6   7    11

findEarliestAncestor(parentChildPairs4, 8) => 4
findEarliestAncestor(parentChildPairs4, 7) => 4
findEarliestAncestor(parentChildPairs4, 6) => 14
findEarliestAncestor(parentChildPairs4, 15) => 14
findEarliestAncestor(parentChildPairs4, 14) => null or -1
findEarliestAncestor(parentChildPairs4, 11) => 4 or 1
n: number of pairs in the input
'''
parentChildPairs3 = [
    (2, 3), (3, 15), (3, 6), (5, 6), (5, 7),
    (4, 5), (4, 8), (4, 9), (9, 11), (14, 4),
]
parentChildPairs4 = [
    (2, 3), (3, 15), (3, 6), (5, 6), (5, 7),
    (4, 5), (4, 8), (4, 9), (9, 11), (14, 2), (1, 9)
]

# parentChildPairs3 = [
#     (2, 3), (3, 15), (3, 6), (5, 6), (5, 7),
#     (4, 5), (4, 8), (4, 9), (9, 11), (14, 4),
# ]
# parentChildPairs4 = [
#     (2, 3), (3, 15), (3, 6), (5, 6), (5, 7),
#     (4, 5), (4, 8), (4, 9), (9, 11), (14, 2), (1, 9)
# ]
def find_ancestors(parents, node, level):
    ancestors = set([])
    for parent in parents[node]:
        ancestors.add((parent, level))
        ancestors = ancestors | find_ancestors(parents, parent, level + 1)
    return ancestors
# def findEarliestAncestor(pairs, node):
#     parents = {}
#     for pair in pairs:
#         parents[pair[0]] = set([])
#         parents[pair[1]] = set([])
#     for pair in pairs:
#         parents[pair[1]].add(pair[0])
#     x_ancestors = find_ancestors(parents, node, 1) # -> (node, level) 
#     ancestor = -1
#     ancestor_level = -1
#     for pair in x_ancestors:
#         if pair[1] > ancestor_level:
#             ancestor = pair[0] 
#             ancestor_level = pair[1]
#     return ancestor

# O(N)
# O(N)
# def helper(pairs):
#     parent_counts =  {}
#     for pair in pairs:
#         parent_counts[pair[0]] = 0
#         parent_counts[pair[1]] = 0
#     for pair in pairs:
#         parent_counts[pair[1]] += 1
#     no_parent = []
#     one_parent = []
#     for key in parent_counts:
#         if parent_counts[key] == 0:
#             no_parent.append(key)
#         elif parent_counts[key] == 1:
#             one_parent.append(key)
#     return [no_parent, one_parent]
# # print(helper(parent_child_pairs))
from collections import deque

def helper(pairs):
	adj = {}
	for d,a in pairs:
		if a in adj:
			adj[a].append(d)
		else:
			adj[a] = [d]
	return adj

def findEarliestAncestor1(pairs, node):
    adj = helper(pairs)
    visited = set()
    visit = deque()
    visit.append((node, 0))
    visited.add(node)
    furthest_node = -1
    furthest_distance = 0
    while len(visit) > 0:
        v,d = visit.pop()
        if d > furthest_distance:
            furthest_node = v
            furthest_distance = d
        if v in adj:
            for neighbor in adj[v]:
                if neighbor not in visited:
                    visit.append((neighbor, d+1))
                    visited.add(neighbor)
    return furthest_node

def buildTree(pairs):
    tree={}
    for parent, child in pairs:

        if child not in tree:
            tree[child]=[parent]
        else:
            tree[child]=tree[child]+[parent]
    return tree

print(buildTree(parentChildPairs3))

def keywithmaxval(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]

def findEarliestAncestor(pairs,node,depth=0):

    tree=buildTree(pairs)
    #run dfs from node
    if node not in tree: 
        if depth == 0:
            return [-1, -1]
        else:
            return [node, depth]

    ancestors={}
    for parent in tree[node]:
        values=findEarliestAncestor(pairs,parent,depth=depth+1)
        ancestors[values[0]]=values[1]
        
    return [max(ancestors,key=ancestors.get),ancestors[max(ancestors,key=ancestors.get)]]




print(findEarliestAncestor(parentChildPairs3, 8))
print(findEarliestAncestor(parentChildPairs3, 7))
print(findEarliestAncestor(parentChildPairs3, 6))
print(findEarliestAncestor(parentChildPairs3, 15))
print(findEarliestAncestor(parentChildPairs3, 14))
print(findEarliestAncestor(parentChildPairs3, 11))