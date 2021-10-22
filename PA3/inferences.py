def inference(self, csp, queue=None): # AC3 algorithm
    queue = {(Xi,Xj) for Xi in list(csp.variables) for Xj in csp.graph[Xi]}

    while queue:
        (Xi,Xj) = queue.pop()
        revised, domain_removal = self.revise(csp,Xi,Xj)
        if revised:
            if len(csp.domain[Xi])==0:
                return False, domain_removal
            for neighbor in csp.graph[Xi]:
                if neighbor != Xj:
                    queue.add((neighbor,Xi))
        else:
            csp.domain[Xi]+=[domain_removal[1]]
    return True, domain_removal

def revise(self, csp, Xi, Xj):
    revised = False
    domain_removal = [Xi,0]
    for value in csp.domain[Xi]:
        conflict = True
        for value2 in csp.domain[Xj]:
            if value != value2:
                conflict = False
                break
        if conflict:
            csp.domain[Xi].remove(value)
            revised = True
            domain_removal[1]=value

    return revised, domain_removal

def add_inferences(self, csp, assignment):
    assignment_additions = []

    for variable in csp.domain.keys():
        
        if len(csp.domain[variable]) == 1:
            assignment[variable] = csp.domain[variable][0]
            assignment_additions += [variable]
    return assignment_additions

def remove_inferences(self, csp, assignment, domain_removal, assignment_additions):

    if domain_removal[1] not in csp.domain[domain_removal[0]]:
        csp.domain[domain_removal[0]] += [domain_removal[1]]

    for variable in list(assignment.keys()):
        if variable in assignment_additions:
            del assignment[variable]
