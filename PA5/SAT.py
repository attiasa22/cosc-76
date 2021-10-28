from random import seed, randint, uniform, choice
class SAT:

    def __init__(self, filename):
        self.file_name = filename
        self.solution = None

    def walksat(self):
         # input: a set of clauses a, max flips, and max tries
        # output: if found, a truth assignment of a
        variables, clauses = self.read_cnf()
        h = 0.7
        seed(1)
        max_tries = 10000
        for i in range(max_tries):
            print(i)
            # Start with a random assignment
            T = {variable:randint(0, 1) for variable in variables}

            max_flips = 100000
            for j in range(max_flips):
                print(j)
               
                satisfied, unsatisfied_clauses = self.find_unsatisfied_clauses(T, clauses)
                 # if T satisfies a then return T
                if satisfied:
                    self.solution = T
                    return T
                clause = choice(unsatisfied_clauses)
                if uniform(0,1) >= h:
                    chosen_variable = choice(list(clause.keys()))
                    T[chosen_variable] = (T[chosen_variable] + 1) % 2 
                else:
                    # p = propositional variable such that a change in its truth assignment 
                    # gives the largest increase in the total number of clauses of a that are
                    # satisfies by T
                    
                    p = self.find_p(T, clauses, clause)

                    # T = T with p reversed
                    T[p] = (T[p] + 1) % 2 

        return "FAILURE"

    def gsat(self, max_flips, max_tries):
        # input: a set of clauses a, max flips, and max tries
        # output: if found, a truth assignment of a

        variables, clauses = self.read_cnf()
        h = 0.7
        seed(1)
        for i in range(max_tries):
            print(i)
            # Start with a random assignment
            T = {variable:randint(0, 1) for variable in variables}

            for j in range(max_flips):
                print(j)
                # if T satisfies a then return T
                if self.satisfies(T, clauses):
                    self.solution = T
                    return T

                if uniform(0,1) >= h:
                    p = choice(list(T.keys()))
                    T[p] = (T[p] + 1) % 2 
                else:
                    # p = propositional variable such that a change in its truth assignment 
                    # gives the largest increase in the total number of clauses of a that are
                    # satisfies by T
                    p = self.find_p(T, clauses, variables)

                    # T = T with p reversed
                    T[p] = (T[p] + 1) % 2 

        return "FAILURE"

    def satisfies(self, T, clauses):
       
        for clause in clauses:
            if not self.clause_satisfied(T, clause):
                return False

        return True

    def find_unsatisfied_clauses(self, T, clauses):
        satisfied = True
        unsatisfied_clauses = []
        for clause in clauses:
            if not self.clause_satisfied(T, clause):
                satisfied = False
                unsatisfied_clauses.append(clause)
        return satisfied, unsatisfied_clauses

    def find_p(self, T, clauses, variables):
        potential_p = []
        max_satisfied_clauses = float("-inf")
        for variable in variables:
            satisfied_clauses = 0
            #(0+1)%2=1, (1+1)%2 = 0
            T[variable] = (T[variable] + 1) % 2 
            for clause in clauses:
                if self.clause_satisfied(T, clause):
                    satisfied_clauses+=1
            
            if satisfied_clauses == max_satisfied_clauses:
                potential_p.append(variable)
        
            elif satisfied_clauses > max_satisfied_clauses:
                potential_p = [variable]
                max_satisfied_clauses = satisfied_clauses

            #flip variable back for next loop
            T[variable] = (T[variable] + 1) % 2

        return choice(potential_p)

    def clause_satisfied(self, T, clause):
        # go through each variable in a clause
        for variable in clause:
            if clause[variable] == T[variable]:
                # return True if at least one variable's truth value is the same as in T
                # this is because CNFs are OR-clauses
                return True
        return False 
            
    def read_cnf(self):
        clauses = []
        variables = set()
        with open(self.file_name, "r") as f:
             for line in f:
                clause={}
                
                stripped_line = line.split()
                
                for word in stripped_line:
                    if word[0] == "-":
                        clause[word[1:]]=0
                        variables.add(word[1:])
                    else:
                         clause[word]=1
                         variables.add(word)
                
                clauses.append(clause)

        return list(variables), clauses


    def write_solution(self, sol_filename):
        with open(sol_filename, 'w') as f:
            for variable in self.solution:
                if self.solution[variable]:
                     f.write(variable+"\n")
                else:
                    f.write("-%s"%variable+"\n")
