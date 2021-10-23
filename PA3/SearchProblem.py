from heuristics import select_unassigned_variable, order_domain_values
from inferences import inferencing, add_inferences, remove_inferences

class SearchProblem():
    def __init__(self, search_problem = None, variable_heuristic = None , value_heuristic = None, should_inference = False):
        self.search_problem = search_problem 
        self.variable_heuristic = variable_heuristic
        self.value_heuristic = value_heuristic
        self.state_visited = 0
        self.should_inference = should_inference

    def backtracking_search(self):
        return self.backtrack(self.search_problem, self.search_problem.assignment)
    
    def backtrack(self, csp, assignment): # returns a solution or failure
        # if assignment is complete then return it
        if self.assignment_complete(csp,assignment):
            print(self.state_visited)
            return assignment
        self.state_visited += 1
        # select an unassigned variable
        current_variable = select_unassigned_variable(csp, assignment, self.variable_heuristic)
        # for each value in the variable's ordered domain
        for value in order_domain_values(csp,current_variable,assignment, self.value_heuristic):
            # if the value is consistent with the current assignment
            if csp.consistency_check(assignment, csp, current_variable, value):
                # add the variable - value pair to the assignment
                assignment[current_variable] = value
                csp.domain[current_variable] = [value]

                # if the user would like to inference
                if self.should_inference:
                    # determine if the inference should be done, as well as the inferences made
                    inference, removed = inferencing(csp)
                    if inference: # if inferences don't lead to failure
                        assignment_additions = add_inferences(csp) # add inferences
                        result = self.backtrack(csp, assignment) # back track

                        if result != "FAILURE":
                            return result
                        # if result is failure, remove inferences from csp
                    remove_inferences(csp, removed)
                    #remove current variable assignment
                    if current_variable in assignment:
                        del assignment[current_variable]
                else:
                    result = self.backtrack(csp, assignment)
                   
                    if result != "FAILURE":
                        return result
                    del assignment[current_variable]
                    csp.domain[current_variable] = csp.values

        return "FAILURE"

    def assignment_complete(self,csp,assignment):
        if csp.variables == set(assignment.keys()):
            return 1
        return 0
