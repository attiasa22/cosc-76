class CircuitBoardFitting():
    def __init__(self, height, width, chips):
        self.width = width
        self.height = height
        self.chips = chips
        self.assignment = {}
        self.variables = self.initialize_variables(height,width)
        self.domains = self.initialize_domains(self.variables, chips)

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
        print(domains)
        return domains

    def consistency_check(self, assignment, csp, current_variable, value):
        left_x = current_variable[1]
        bottom_y = current_variable[0]
        right_x = current_variable[1]+value[1]
        top_x = current_variable[0]+value[0]

        for key in assignment.keys():
            left_x = current_variable[1]
            bottom_y = current_variable[0]
            right_x = current_variable[1]+value[1]
            top_x = current_variable[0]+value[0]





    def draw_board(self, assignment):
        for i in range(self.height):
            string=""
            for j in range(self.width):
                