class MapColoring():
    def __init__(self, map_boundaries, colors):
        self.graph = map_boundaries
        self.assignment = {}
        self.variables = set(map_boundaries.keys())
        self.values = list(range(1,colors+1))
        self.domain = {k:self.values for k in self.variables}

    def consistency_check(self, assignment, csp, current_variable, value):
        for key in assignment.keys():
            if key in csp.graph[current_variable] and assignment[key] == value:
                return 0
        return 1

    def revise_check(self, value2, value):
        return value != value2

    def fix_domains(self):
        pass

    def assignment_complete(self,csp,assignment):
        if csp.variables == set(assignment.keys()):
            return 1
        return 0