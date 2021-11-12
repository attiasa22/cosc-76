from random import choice
from Maze import Maze
import numpy as np


class MazeProblem:

    def __init__(self, maze, true_positive):
        self.maze = maze
        # list of all possible floors - the states used by the markov problem
        self.states = maze.find_floors()
        # each floor is evenly likely at the start
        self.initial_distribution = self.initialize_matrix()
        # set a random initial state for the robot
        self.current_state = self.set_random_start() 
        # odds sensor is correct
        self.color_probability = true_positive
        # list of distributions
        self.solution = [self.initial_distribution]
        self.veterbi_solution = []
        # robot's path
        self.true_states = [self.current_state]
        self.observation_space = {"R":0, "G":1, "B":2, "Y":3}
        self.observations = [str(self.maze.get_floor( self.current_state[0],self.current_state[1]))]


    def __str__(self):
        string =  "Mazeworld Markov problem: "
        return string

    def initialize_matrix(self):
        initial_distribution = 1/len(self.states)
        distribution_matrix = np.array([initial_distribution]*len(self.states))

        return distribution_matrix

    def set_random_start(self): 
        if len(self.states)==0 or len(self.states)==1: 
            print("No HMM necessary")
        
        return choice(self.states)

    def get_new_state(self):
        # get current state coordinates
        x = self.current_state[0]
        y = self.current_state[1]

        # randomly choose movement to new state
        new_state = choice([[x+1,y], [x-1,y], [x,y+1], [x,y-1]])
        
        if not self.maze.is_floor(new_state[0], new_state[1]):
            new_state = self.current_state
        chosen_floor_color = self.maze.get_floor(new_state[0], new_state[1])
        other_colors = set(["R", "G", "B", "Y"]).difference(set(chosen_floor_color))

        inverse_p = (1-self.color_probability)/3
        p_distribution = [self.color_probability,inverse_p,inverse_p,inverse_p]
        new_color = np.random.choice([chosen_floor_color]+list(other_colors),p = p_distribution)

        self.true_states += [new_state]
        self.observations += [new_color]
        
        return new_color

    def show_solution(self):
        for i in range(len(self.solution)):

            probability_matrix = np.zeros((self.maze.height,self.maze.width))

            self.maze.robotloc[0] = self.true_states[i][0]
            self.maze.robotloc[1] = self.true_states[i][1]
            self.maze.create_render_list()

            print("Current Position: " + str(self.maze.robotloc))
            if len(self.veterbi_solution):
                print("Veterbi Position: " + str(self.states[int(self.veterbi_solution[i])]))
            print("Percieved Color: " + str(self.observations[i]))
            print("Real Color: " + str(self.maze.get_floor( self.maze.robotloc[0],self.maze.robotloc[1])))
            print("MAZE: \n"+str(self.maze))

            for j in range(len(self.solution[i])):
                probability_matrix[self.states[j][1]][self.states[j][0]] = self.solution[i][j]
            print(np.flip(probability_matrix, 0))

# used for testing
#
# if __name__ == "__main__":
#     test_maze1 = Maze("PA6/maze1.maz")
#     problem = MazeProblem(test_maze1)
#     print(problem.initialize_matrix())
#
