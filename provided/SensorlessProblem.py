from Maze import Maze
from time import sleep

class SensorlessProblem:
    ## You write the good stuff here:
    def __init__(self, maze):
        self.maze = maze
        self.start_state = tuple(self.initbeliefstates())

    def initbeliefstates(self):
        belief_states = []
        # for each cell in a maze
        for i in range(self.maze.width):
            for j in range(self.maze.height): 
                # if the cell is a tile
                if self.maze.is_floor(i,j):
                    # include the cell in our initial belief states
                    belief_states += (i,j)
        return belief_states

    def get_successors(self, belief_states):
        #go through the 4 possible actions and return the belief states they lead to 
        north_action = self.check_successors(0 , 1, belief_states)
        south_action = self.check_successors(0, -1, belief_states)
        east_action = self.check_successors(1, 0, belief_states)
        west_action = self.check_successors(-1, 0, belief_states)

        return [north_action] + [south_action] + [east_action] + [west_action]

    def check_successors(self, x_change, y_change, belief_states):
        visited = set()
        successors = []

        #for each location
        for index in range(0, len(belief_states), 2):
            #determine the potential new belief state
            new_x = belief_states[index]+x_change
            new_y = belief_states[index+1]+y_change

            if self.maze.is_floor(new_x,new_y):
                successors+=(new_x, new_y)
                visited.add((new_x,  new_y))
            #if the new action leads to an impossible belief state, and there already isnt a robot here
            elif (belief_states[index],  belief_states[index+1]) not in visited:
                #add the current location as well
                successors+=(belief_states[index],  belief_states[index+1])
                visited.add((belief_states[index],  belief_states[index+1]))
        return list(successors)

    def goal_test(self,belief_states):
        if len(belief_states) == 2:
            return True
        return False 

    def heuristic_fn(self, successor_states):
        return len(successor_states)

    def __str__(self):
        string =  "Blind robot problem: "
        return string

    # given a sequence of states (including robot turn), modify the maze and print it out.
    #  (Be careful, this does modify the maze!)
    def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robotloc = tuple(self.start_state)

        for state in path:
            print(str(self))
            self.maze.robotloc = tuple(state)
            sleep(1)

            print(str(self.maze))
