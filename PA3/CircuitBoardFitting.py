class CircuitBoardFitting():
    def __init__(self, height, width, chips):
        self.chips=chips
        self.width = width
        self.height = height
        self.values = [(i,j) for i in range(height) for j in range(width)]
        self.assignment = {}
        self.variables = set(chips.keys())
        self.domain = self.initialize_domains(self.variables, width, height)
        self.graph = self.create_graph(self.chips)

    # creates a constraint graph similar to the map coloring. 
    def create_graph(self, chips):
        graph = {k:[] for k in chips.keys()}
        
        for key in graph.keys():
            graph[key] = list(set(graph.keys()).difference(set(key)))

        return graph

    # Each chip's domain contains all the possible lower left corners it can be
    def initialize_domains(self, variables, width,height):
        domains ={k:[] for k in variables}
        for i in range(height):
            for j in range(width):
                for variable in variables:
                        if self.chips[variable][0]+i<=self.height and self.chips[variable][1]+j<=self.width:
                            domains[variable]+=[(i,j)]

        return domains

    # Check if the chip is not overlapping on another chip and is on the board properly
    def consistency_check(self, assignment, csp, current_variable, value):
        consistent = True
        # Find the coordinates of each edge
        left_x = value[1]
        bottom_y =value[0]
        right_x = self.chips[current_variable][1] + value[1]
        top_y = self.chips[current_variable][0] + value[0]

        out_of_bounds = False
        overlaps = False
        # For each already assigned chip
        for key in assignment.keys():

            left_x2 = assignment[key][0][1]
            bottom_y2 = assignment[key][0][0]
            right_x2 = self.chips[key][1]+assignment[key][0][1]
            top_y2 = self.chips[key][0]+assignment[key][0][0]
            # If the chips are overlapping
            if not (left_x2>=right_x or left_x>=right_x2 or bottom_y2>=top_y or bottom_y>=top_y2):
                overlaps = True
        # If the chip is off the board
        if top_y>self.height or  right_x>self.width:
            out_of_bounds = True

        if overlaps or out_of_bounds:
            consistent = False

        return consistent
    
    # Print out the board ASCII Art style
    def draw_board(self):
        assignment = self.assignment
        #Go top row to bottom row
        for i in range(self.height-1,-1, -1):
            string=""
            # Left to right
            for j in range(self.width):
                added_letter=False
                # Check each chip for this coordinate
                for key in assignment.keys():
                    left_x = assignment[key][0][1]
                    bottom_y = assignment[key][0][0]
                    right_x = self.chips[key][1]+assignment[key][0][1]
                    top_y = self.chips[key][0]+assignment[key][0][0]

                    if i<top_y and i>= bottom_y and j>=left_x and j<right_x:
                        string+=key
                        added_letter=True

                if not added_letter:
                    string+="."

            print(string)
                