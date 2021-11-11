from random import choice
from Maze import Maze
import numpy as np


class MazeProblem:

    def __init__(self, maze):
        self.maze = maze
        # list of all possible floors - the states used by the markov problem
        self.list_of_floors = maze.find_floors()
        # each floor is evenly likely at the start
        self.initial_distribution = self.initialize_matrix()
        # set a random initial state for the robot
        self.current_state = self.set_random_start() 
        # odds sensor is correct
        self.color_probability = 0.88
        
        # list of distributions
        self.solution = [self.initial_distribution]
        # robot's path
        self.true_states = [self.current_state]

        self.observed_color = [str(self.maze.get_floor( self.current_state[0],self.current_state[1]))]

    def __str__(self):
        string =  "Mazeworld Markov problem: "
        return string

    def initialize_matrix(self):
        initial_distribution = 1/len(self.list_of_floors)
        distribution_matrix = np.array([initial_distribution]*len(self.list_of_floors))

        return distribution_matrix

    def set_random_start(self): 
        if len(self.list_of_floors)==0 or len(self.list_of_floors)==1: 
            print("No HMM necessary")
        
        return choice(self.list_of_floors)

    def show_solution(self):
       
        for i in range(len(self.solution)):
            probability_matrix = np.zeros((self.maze.height,self.maze.width))
            self.maze.robotloc[0] = self.true_states[i][0]
            self.maze.robotloc[1] = self.true_states[i][1]
            self.maze.create_render_list()
            print("Current Position: " + str(self.maze.robotloc))
            print("Percieved Color: " + str(self.observed_color[i]))
            print("Real Color: " + str(self.maze.get_floor( self.maze.robotloc[0],self.maze.robotloc[1])))
            print("MAZE: \n"+str(self.maze))

            for j in range(len(self.solution[i])):
                probability_matrix[self.list_of_floors[j][1]][self.list_of_floors[j][0]] = self.solution[i][j]
            print(np.flip(probability_matrix, 0))





if __name__ == "__main__":
    test_maze1 = Maze("PA6/maze1.maz")
    problem = MazeProblem(test_maze1)
    print(problem.initialize_matrix())
