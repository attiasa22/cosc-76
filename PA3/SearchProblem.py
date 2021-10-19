from copy import deepcopy
from random import choice
class SearchProblem():
    def __init__(self, search_problem = None, variable_heuristic = None , value_heuristic = None, inference = 0):
        self.search_problem = search_problem 
        self.variable_heuristic = variable_heuristic
        self.value_heuristic = value_heuristic
        self.state_visited = 0
        self.inference = inference

    def backtracking_search(self):
        return self.backtrack(self.search_problem, self.search_problem.assignment)
    
    def backtrack(self, csp, assignment):
        csp_copy = deepcopy(csp)
        if self.assignment_complete(csp,assignment):
            #print(self.state_visited)
            return assignment
        current_variable = self.select_unassigned_variable(csp, assignment, self.variable_heuristic)
        
        #print(self.order_domain_values(csp,current_variable,assignment, self.value_heuristic))
        for value in self.order_domain_values(csp,current_variable,assignment, self.value_heuristic):
            if csp.consistency_check(assignment, csp, current_variable, value):
                assignment[current_variable] = value
                csp.domain[current_variable] = [value]

                if self.inference:

                    inferences = self.inference(csp, current_variable, assignment)

                    if not self.check_inference_failure(inferences):
                        self.add_inferences(inferences, csp)
                        result = self.backtrack(csp, assignment)
                    
                        if self.check_csp_failure(result):
                            return result
                else:
                    #self.state_visited+=1
                    result = self.backtrack(csp, assignment)
                   
                    #if check_csp_failure(result):
                    #print(result)
                    if result != "FAILURE":
                        return result
                    del assignment[current_variable]
                    csp.domain[current_variable] = csp.values
                    #csp=csp_copy
               
                   
           
                
           
        #if self.assignment_complete(csp,assignment):
        #    print(self.state_visited)
        #    return assignment

        return "FAILURE"

    #compare the set of variables to the set of assignments made
    def assignment_complete(self,csp,assignment):
        if csp.variables == set(assignment.keys()):
            return 1
        return 0

    def select_unassigned_variable(self, csp, assignment, heuristic):
        if heuristic is None:
            unassigned_variables = csp.variables.difference(set(assignment.keys()))
            return list(unassigned_variables)[0]
        else:
            return eval("self.%s"%heuristic)(csp, assignment)
    
    def order_domain_values(self, csp,current_variable,assignment, heuristic):
        if heuristic is None:
            unassigned_values = csp.domain[current_variable]
            return list(unassigned_values)
        else:
            return eval("self.%s"%heuristic)(csp, current_variable)
            
    def mrv(self, csp, assignment):
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
         
    
    def degree_heuristic(self,csp,assignment):
        relevant_variables = {}
        for variable in csp.graph.keys():
            if variable not in assignment.keys():
                relevant_variables[variable]=len(csp.graph[variable])
        return max(relevant_variables.items(), key= lambda x: x[1])[0]

    def lcv(self,csp, current_variable):
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

    def inference(self, csp, current_variable,assignment):
        pass

    def check_inference_failure(self, inferences):
        pass

    def add_inferences(self, inferences, csp):
        pass

    def check_csp_failure(self, result):
        pass