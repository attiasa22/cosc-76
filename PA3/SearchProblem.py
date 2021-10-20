from heuristics import select_unassigned_variable, order_domain_values

class SearchProblem():
    def __init__(self, search_problem = None, variable_heuristic = None , value_heuristic = None, should_inference = False):
        self.search_problem = search_problem 
        self.variable_heuristic = variable_heuristic
        self.value_heuristic = value_heuristic
        self.state_visited = 0
        self.should_inference = should_inference

    def backtracking_search(self):
        return self.backtrack(self.search_problem, self.search_problem.assignment)
    
    def backtrack(self, csp, assignment):

        if csp.assignment_complete(csp,assignment):
            return assignment

        current_variable = select_unassigned_variable(csp, assignment, self.variable_heuristic)
        
        for value in order_domain_values(csp,current_variable,assignment, self.value_heuristic):
            if csp.consistency_check(assignment, csp, current_variable, value):
                assignment[current_variable] = value
                csp.domain[current_variable] = [value]
                csp.fix_domains()
                if self.should_inference:
                    
                    inference, domain_removal = self.inference(csp)

                    if inference: # if inferences don't lead to failure

                        assignment_additions = self.add_inferences(csp, assignment) # add inferences
                        result = self.backtrack(csp, assignment) # back track

                        if result != "FAILURE": # if result isn't a failure
                            return result
                        #remove inferences from csp
                        self.remove_inferences(csp, assignment, domain_removal, assignment_additions)
                    #remove current variable assignment
                    if current_variable in assignment:
                        del assignment[current_variable]
                    csp.domain[current_variable] = csp.values
                else:
                    #self.state_visited+=1
                    result = self.backtrack(csp, assignment)
                   
                    if result != "FAILURE":
                        return result
                    del assignment[current_variable]
                    csp.domain[current_variable] = csp.values
                csp.fix_domains()

        return "FAILURE"

    def inference(self, csp, queue=None):
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
                if csp.revise_check(value2, value):
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
            
            if len(csp.domain[variable])==1:
                assignment[variable]=csp.domain[variable][0]
                assignment_additions+=[variable]

        return assignment_additions

    def remove_inferences(self, csp, assignment, domain_removal, assignment_additions):
        # domain_removals = {k:[] for k in csp.variables}
        # assignment_additions = []

        if domain_removal[1] not in csp.domain[domain_removal[0]]:
            csp.domain[domain_removal[0]]+=[domain_removal[1]]

        for variable in list(assignment.keys()):
            if variable in assignment_additions:
                del assignment[variable]