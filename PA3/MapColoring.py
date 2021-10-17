class MapColoring():
    def __init__(self, map_boundaries, colors):
        self.map_boundaries = map_boundaries #initial 
        self.colors = colors
        self.assignment = {}

    def consistency_check(self,assignment, csp, current_variable, value):
        for key in assignment.keys():
            if key in csp.graph[current_variable] and assignment[key] == value:
                return 0
        return 1

    def get_possible_colors(self, colored_map, country):
        pass

    def check_possible_color(self,colored_map, country, color):
        pass

    def goal_test(self, map):
        pass