

from copy import deepcopy
def select_unassigned_variable(csp, assignment, heuristic):
    if heuristic is None:
        unassigned_variables = csp.variables.difference(set(assignment.keys()))
        return list(unassigned_variables)[0]
    else:
        return eval("%s"%heuristic)(csp, assignment)

def order_domain_values(csp,current_variable,assignment, heuristic):
    if heuristic is None:
        unassigned_values = csp.domain[current_variable]
        return list(unassigned_values)
    else:
        return eval("%s"%heuristic)(csp, current_variable)
        
def mrv(csp, assignment):
    relevant_variables = {}
    domain_copy = deepcopy(csp.domain)
    for key in assignment.keys():
        for neighbors in csp.graph[key]:
            if assignment[key] in domain_copy[neighbors]:
                domain_copy[neighbors].remove(assignment[key])
            if len(domain_copy[neighbors])>1:
                relevant_variables[neighbors]=len(domain_copy[neighbors])

    if len(relevant_variables.keys()) >0:
        return min(relevant_variables.items(), key= lambda x: x[1])[0]
    unassigned_variables = csp.variables.difference(set(assignment.keys()))
    return list(unassigned_variables)[0]
        

def degree_heuristic(csp,assignment):
    relevant_variables = {}
    for variable in csp.graph.keys():
        if variable not in assignment.keys():
            relevant_variables[variable]=len(csp.graph[variable])
    return max(relevant_variables.items(), key= lambda x: x[1])[0]

def lcv(csp, current_variable):
    relevant_values= {k:0 for k in csp.values}
    #print(csp.domain[current_variable])
    for value in csp.values:
        
        for neighbor in csp.graph[current_variable]:
            if value in csp.domain[neighbor]:
                if value in relevant_values:
                    relevant_values[value]=relevant_values[value]+1
    
    if len(relevant_values.keys())>0:
        return sorted(relevant_values,key= relevant_values.get, reverse=False)
    else:
        #print("unassigned")
        unassigned_values = csp.values
        return list(unassigned_values)

