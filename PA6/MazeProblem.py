from random import choice
from Maze import Maze
import numpy as np


class MazeworldProblem:

    def __init__(self, maze):
        self.maze = maze
        self.list_of_floors = maze.find_floors()
        self.distribution = self.initialize_matrix()
        self.current_state = self.set_random_start() 
        self.solution = [self.distribution]
        self.color_probability = 0.88
        self.true_states = [self.start_state]

    def __str__(self):
        string =  "Mazeworld Markov problem: "
        return string

    def initialize_matrix(self):
        initial_distribution = 1/len(self.list_of_floors)
        distribution = np.diag(np.array([initial_distribution]*len(self.list_of_floors)))
        print(distribution)
        return distribution

    def set_random_start(self): 
        if len(self.list_of_floors)==0 or len(self.list_of_floors)==1: 
            return self.goal_test()
        
        return choice(self.list_of_floors)

    def goal_test(self):
        if len(self.list_of_floors)==0:
            return "NO FLOORS"

        if all(v == 0 for v in self.distribution):
            return "FAILURE"

        if len(set(self.distribution).difference(set(0))) == 1:
            return self.solution

        else: 
            return 0


if __name__ == "__main__":
    test_maze1 = Maze("PA6/maze1.maz")
    problem = MazeworldProblem(test_maze1)
    print(problem.initialize_matrix().size)
    print(test_maze1.is_floor(1,2))

