def inferencing(csp, queue=None): # AC3 algorithm
    queue = [(Xi,Xj) for Xi in list(csp.variables) for Xj in csp.graph[Xi]]
    removed = []
    while len(queue):

        (Xi,Xj) = queue.pop() 
        revised, removed_value = revise(csp, Xi, Xj)

        removed += removed_value

        if revised:
            if len(csp.domain[Xi]) == 0:
                return False, removed

            for neighbor in csp.graph[Xi]:
                if neighbor != Xj:
                    queue += [(neighbor, Xi)]

    return True, removed

def revise(csp, Xi, Xj):
    removed_value = []
    revised = False

    for value in csp.domain[Xi]:
        conflict = True
        for value2 in csp.domain[Xj]:
            if value != value2:
                conflict = False
        
        if conflict:
            revised = True
            removed_value += [(Xi, value)]

            relevant_domain = csp.domain[Xi]
            relevant_domain.remove(value)

    return revised, removed_value

def add_inferences(csp):
    for key in csp.domain.keys():
        if len(csp.domain[key]) == 1:
            csp.assignment[key] = csp.domain[key][0]

def remove_inferences(csp, removed):
    removed = list(filter(None, removed))

    for pair in removed:
        csp.domain[pair[0]] += [pair[1]]

    for key in list(csp.assignment.keys()):
        if len(csp.domain[key]) != 1:
            csp.assignment.pop(key)
    


   