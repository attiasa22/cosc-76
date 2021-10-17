from copy import deepcopy

def SearchProblem():
    def __init__(self, search_problem, variable_heuristic = None , value_heuristic = None, inference = 0):
        self.search_problem = search_problem 
        self.variable_heuristic = variable_heuristic
        self.value_heuristic = value_heuristic


    def backtracking_search(self,):
        return backtrack(self.search_problem, self.search_problem.assignment)
    
    def backtrack(self, csp, assignment):
        if assignment_complete(assignment):
            return assignment
        
        current_variable = select_unassigned_variable(csp, assignment, self.variable_heuristic)
        csp_copy = deepcopy()

        for value in order_domain_values(csp,current_variable,assignment, self.value_heuristic):
            
            if self.search_problem.consistency_check(assignment, csp, current_variable. value):
                assignment[current_variable] = value

                if inference:

                    inferences = inference(csp, current_variable, assignment)

                    if not check_inference_failure(inferences):
                        add_inferences(inferences, csp)
                        result = backtrack(csp, assignment)

                        if check_csp_failure(result):
                            return result
                else:
                    result = backtrack(csp, assignment)

                    #if check_csp_failure(result):
                    return result

                csp = csp_copy

        return 'FAILURE'

    #compare the set of variables to the set of assignments made
    def assignment_complete(self,assignment):
        if self.search_problem.variables == set(assignment.keys()):
            return 1
        return 0

    def select_unassigned_variable(self, csp, assignment, heuristic):
        if heuristic is None:
            unassigned_variables = self.search_problem.variables.difference(set(assignment.keys()))
            return list(unassigned_variables)[0]
        else:
            return heuristic(csp, assignment)
    
    def order_domain_values(self, csp,current_variable,assignment, heuristic):
        if heuristic is None:
            unassigned_values = self.search_problem.values
            return list(unassigned_values)
        else:
            return heuristic(csp, assignment)

    def inference(self, csp, current_variable,assignment):
        pass

    def check_inference_failure(self, inferences):
        pass

    def add_inferences(self, inferences, csp):
        pass

    def check_csp_failure(self, result):
        pass
