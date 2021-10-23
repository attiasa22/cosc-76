

from copy import deepcopy

def select_unassigned_variable(csp, assignment, heuristic):
    if heuristic is None:
        unassigned_variables = csp.variables.difference(set(assignment.keys()))
        return sorted(list(unassigned_variables))[0]

    return eval("%s"%heuristic)(csp, assignment)

def order_domain_values(csp,current_variable,assignment, heuristic):
    if heuristic is None:
        #unassigned_values = csp.domain[current_variable]
        unassigned_values = csp.values
        return list(unassigned_values)

    return sorted(eval("%s"%heuristic)(csp, current_variable))
        
def mrv(csp, assignment):
    relevant_variables = {}

    for key in assignment.keys():
        for neighbors in csp.graph[key]:
            if assignment[key] in csp.domain[neighbors]:
                csp.domain[neighbors].remove(assignment[key])
            if len(csp.domain[neighbors])>1:
                relevant_variables[neighbors]=len(csp.domain[neighbors])

    if len(relevant_variables.keys()) >0:
        return min(relevant_variables.items(), key= lambda x: x[1])[0]

    unassigned_variables = csp.variables.difference(set(assignment.keys()))
    return sorted(list(unassigned_variables))[0] 

def degree_heuristic(csp,assignment):
    relevant_variables = {}
    for variable in csp.graph.keys():
        if variable not in assignment.keys():
            relevant_variables[variable]=len(csp.graph[variable])

    return max(sorted(relevant_variables.items()), key= lambda x: x[1])[0]

def lcv(csp, current_variable):
    relevant_values= {k:0 for k in csp.values}

    for value in csp.values:
        for neighbor in csp.graph[current_variable]:
            if value in csp.domain[neighbor]:
                if value in relevant_values:
                    relevant_values[value]=relevant_values[value]+1
    
    if len(relevant_values.keys())>0:
        return sorted(relevant_values,key= relevant_values.get, reverse=False)

    return list(csp.values)
