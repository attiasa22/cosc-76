from operator import xor
from os import X_OK
import numpy as np
from sklearn.preprocessing import normalize
from random import choice

class MarkovSolver:
    def __init__(self, maze_problem):
        self.maze_problem = maze_problem
        

    def filtering(self):
        f_t = self.maze_problem.distribution
        transition_matrix_transpose = np.transpose(self.transition_matrix())
        while not self.maze_problem.goal_test():
            observation_matrix = self.observation_matrix()

            f_t= normalize((observation_matrix @ transition_matrix_transpose) @ f_t, norm = 'l1')


    # Given S possible states, an S x S matrix T is created, such that T[i][j] is chance that we go from i to j
    # Since our robot takes a random movement in the 4 cardinal directions, that chance is 0.25
    # However, a floor bordering a wall actually has a chance to come from itself, 
    # So any wall encountered is actually an increase of 0.25 to T[i][i]
    def transition_matrix(self):
        dimension = self.maze_problem.maze.width * self.maze_problem.maze.height
        transition_matrix= np.zeros((dimension,dimension))

        for floor in self.list_of_floors:
            index_floor_1 = self.list_of_floors.index(floor)
            x = floor[0] 
            y = floor[1]

            if [x+1,y] in self.list_of_floors:
                index_floor_2 = self.list_of_floors.index([x+1,y])
                transition_matrix[index_floor_2][index_floor_1]= 0.25
            else:
                transition_matrix[index_floor_1][index_floor_1]+= 0.25

            if [x,y+1] in self.list_of_floors:
                index_floor_2 = self.list_of_floors.index([x+1,y])
                transition_matrix[index_floor_2][index_floor_1]= 0.25
            else:
                transition_matrix[index_floor_1][index_floor_1]+= 0.25

            if [x,y-1] in self.list_of_floors:
                index_floor_2 = self.list_of_floors.index([x+1,y])
                transition_matrix[index_floor_2][index_floor_1]= 0.25
            else:
                transition_matrix[index_floor_1][index_floor_1]+= 0.25

            if [x-1,y] in self.list_of_floors:
                index_floor_2 = self.list_of_floors.index([x+1,y])
                transition_matrix[index_floor_2][index_floor_1]= 0.25
            else:
                transition_matrix[index_floor_1][index_floor_1]+= 0.25

        return transition_matrix

    # Create a diagonal S x S matrix where the diagonal values is the odds of that state occuring given a random movement event
    def observation_matrix(self):
        odds = [0]* len(self.list_of_floors)
        x = self.current_state[0]
        y = self.current_state[1]

        new_state = choice([[x+1,y],[x-1,y],[x,y+1],[x,y-1]])

        if not self.maze.maze.is_floor(new_state[0],new_state[1]):
            new_state = self.current_state

        new_color = self.maze.maze.index(new_state[0],new_state[1])


        for index in range(len(self.list_of_floors)):
            if self.maze.maze.index(new_state[0],new_state[1])


