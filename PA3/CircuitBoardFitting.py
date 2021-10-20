class CircuitBoardFitting():
    def __init__(self, height, width, chips):
        self.width = width
        self.height = height
        self.values = chips
        self.assignment = {}
        self.variables = set(self.initialize_variables(height,width))
        self.domain = self.initialize_domains(self.variables, chips)

    def initialize_variables(self, height,width):
        variables=[]
        for i in range(height):
            for j in range(width):
                variables+=[(i,j)]
        print(variables)
        return variables


    def initialize_domains(self, variables, chips):
        domains ={k:[] for k in variables}
        for variable in variables:
            for chip in chips.keys():
                if variable[0]+chips[chip][0]<=self.height and variable[1]+chips[chip][1]<=self.width:
                    domains[variable]+=[chip]
       # print(domains)
        return domains

    def consistency_check(self, assignment, csp, current_variable, value):
        #print(current_variable)
        #print(value)
        #print(self.values[value])
        left_x = current_variable[1]
        bottom_y = current_variable[0]
        right_x = current_variable[1]+self.values[value][1]
        top_y = current_variable[0]+self.values[value][0]

        overlaps = False

        for key in assignment.keys():
            left_x2 = key[1]
            bottom_y2 = key[0]
            right_x2 = key[1]+self.values[assignment[key]][1]
            top_y2 = key[0]+self.values[assignment[key]][0]

            if not (left_x2>right_x or left_x>right_x2 or bottom_y2>top_y or bottom_y>top_y2):
                overlaps = True

        if overlaps:
            return False
        return True



    def fix_domains(self):
        self.domain = self.initialize_domains(self.variables, self.values)

        for value in self.assignment.values():
            for variable in self.domain.keys():
                if value in self.domain[variable]:
                    self.domain[variable].remove(value)
                if variable in self.assignment.keys():
                    self.domain[variable]=[value]
    
    def assignment_complete(self,csp,assignment):
        if csp.values == set(assignment.values()):
            return 1
        return 0
        
   # def draw_board(self, assignment):
   #     for i in range(self.height):
   #         string=""
   #         for j in range(self.width):
                