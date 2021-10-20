class CircuitBoardFitting2():
    def __init__(self, height, width, chips):
        self.chips=chips
        self.width = width
        self.height = height
        self.values = [(i,j) for i in range(height) for j in range(width)]
        self.assignment = {}
        self.variables = set(chips.keys())
        self.domain = self.initialize_domains(self.variables, width, height)

    def initialize_domains(self, variables, width,height):
        domains ={k:[] for k in variables}
        for i in range(height):
            for j in range(width):
                for variable in variables:
                        if self.chips[variable][0]+i<=self.height and self.chips[variable][1]+j<=self.width:
                            domains[variable]+=[(i,j)]

        return domains

    def consistency_check(self, assignment, csp, current_variable, value):


        left_x = value[1]
        print(left_x)
        bottom_y =value[0]
        print(bottom_y)
        right_x = self.chips[current_variable][1]
        print(right_x)
        top_y = self.chips[current_variable][0]
        print( top_y )

        overlaps = False
        print(assignment)
        for key in assignment.keys():
            left_x2 = assignment[key][1]
            print(left_x2)
            bottom_y2 = assignment[key][0]
            print(bottom_y2)
            right_x2 = self.chips[key][1]+assignment[key][1]
            print(right_x2)
            top_y2 = self.chips[key][0]+assignment[key][0]
            print( top_y2)

            if not (left_x2>=right_x or left_x>=right_x2 or bottom_y2>=top_y or bottom_y>=top_y2):
                overlaps = True

        if overlaps:
            return False
        return True



    def fix_domains(self):
        self.domain = self.initialize_domains(self.variables, self.width,self.height)

        for value in self.assignment.values():
            for variable in self.domain.keys():
                if value in self.domain[variable]:
                    self.domain[variable].remove(value)
                if variable in self.assignment.keys():
                    self.domain[variable]=[value]
    
    def assignment_complete(self,csp,assignment):
        if csp.variables == set(assignment.keys()):
            return 1
        return 0
        
   # def draw_board(self, assignment):
   #     for i in range(self.height):
   #         string=""
   #         for j in range(self.width):
                