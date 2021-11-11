import numpy as np
from sklearn.preprocessing import normalize
from random import choice
from MazeProblem import MazeProblem
from Maze import Maze

class MarkovSolver:

    def __init__(self, maze_problem):
        self.maze_problem = maze_problem
        

    def filtering(self):
        # this function continuously applies the matrix transformation version
        # f_1:t+1 = a(O_t+1)(T_transpose)(f_1:t)
        f_t = self.maze_problem.initial_distribution
        transition_matrix_transpose = self.transition_matrix().T
        # apply the HMM a certain number of times
        for i in range(3):
            observation_matrix = self.observation_matrix()
            #sci_kit learn's normalize function performs the same action as a in the equation
            f_t = normalize(((observation_matrix @ transition_matrix_transpose) @ f_t).reshape(-1,1), axis=0, norm = 'l1')
            self.maze_problem.solution += [f_t]
        

    def viterbi(self):
        color_map = {"R":0, "G":1, "B":2, "Y":3}
        observations =  self.maze_problem.observed_color
        print(len(observations))
        transition_matrix = self.transition_matrix()
        print(transition_matrix.shape)
        emission_matrix = self.emission_matrix()
        print(emission_matrix.shape)
        initial_probabilities = self.maze_problem.initial_distribution
        
        state_size = len(self.maze_problem.list_of_floors)
        observation_count = len(observations)
        T1 = np.zeros((state_size, observation_count))
        T2 = np.zeros((state_size, observation_count))
        T1[:, 0] = initial_probabilities * emission_matrix[:, color_map[observations[0]]]

        for i in range(observation_count):
            T1[:][i] = np.max(T1[:][i - 1] * transition_matrix.T * emission_matrix[:][color_map[observations[i]]].T, 1)
            T2[:][i] = np.argmax(T1[:][i - 1] * transition_matrix.T, 1)
        solution = np.zeros(observation_count)
        solution[-1] = np.argmax(T1[:, observation_count - 1])

        for i in reversed(range(1,observation_count )):
            solution[i - 1] = T2[int(solution[i]), i]
        print(solution)
        return solution
    # Given S possible states, an S x S matrix T is created, such that T[i][j] is chance that we go from i to j
    # Since our robot takes a random movement in the 4 cardinal directions, that chance is 0.25
    # However, a floor bordering a wall actually has a chance to come from itself, 
    # So any wall encountered is actually an increase of 0.25 to T[i][i]
    def transition_matrix(self):
        # initialize a S xS matrix of zeros
        dimension = len(self.maze_problem.list_of_floors)
        transition_matrix= np.zeros((dimension,dimension))
        # for each state
        for floor in self.maze_problem.list_of_floors:
            index_floor_1 = self.maze_problem.list_of_floors.index(floor)
            x = floor[0] 
            y = floor[1]
            # determine if neighboring cells are possible previous states
            self.set_matrix(transition_matrix, index_floor_1, x+1, y)
            self.set_matrix(transition_matrix, index_floor_1, x-1, y)
            self.set_matrix(transition_matrix, index_floor_1, x, y+1)
            self.set_matrix(transition_matrix, index_floor_1, x, y-1)

        return transition_matrix

    def set_matrix(self, transition_matrix, index_floor_1, x, y):
        # if the cell is a state
        if [x,y] in self.maze_problem.list_of_floors:
                # set T[i][j] to probabilty of transition
                index_floor_2 = self.maze_problem.list_of_floors.index([x,y])
                transition_matrix[index_floor_2][index_floor_1] = 0.25
        else:
            # if the cell is not a state
            # the movement will leave the robot in the same state
            # meaning that the state is reachable from itself
            transition_matrix[index_floor_1][index_floor_1] += 0.25

    # Create a diagonal S x S matrix 
    # where the diagonal values are the odds of that state occuring 
    # given a random movement event
    def observation_matrix(self):
        # initialize a 1 x S matrix
        # where each cell i is an observation probability of state i
        odds = [0]* len(self.maze_problem.list_of_floors)
        
        new_color = self.get_new_color()
        # for each state
        for index in range(len(self.maze_problem.list_of_floors)):
            # if state is the same as the observed state
            if self.maze_problem.maze.get_floor(self.maze_problem.list_of_floors[index][0],self.maze_problem.list_of_floors[index][1]) == new_color:
                # add the probability it will be sensed correctly
                odds[index] = self.maze_problem.color_probability
            else:
                odds[index] = 1 - self.maze_problem.color_probability

        # O matrix is the S x S matrix whose diagonals are the observation probabilities
        observational_matrix = np.diag(odds)

        return observational_matrix

    def emission_matrix(self):
        color_map = {"R":0, "G":1, "B":2, "Y":3}
        emission_matrix = np.full((len(self.maze_problem.list_of_floors), 4), 0.12)

        for i in range((len(self.maze_problem.list_of_floors))):
            
            j= color_map[self.maze_problem.maze.get_floor(self.maze_problem.list_of_floors[i][0],self.maze_problem.list_of_floors[i][1])]
            emission_matrix[i,j] = self.maze_problem.color_probability

        return emission_matrix

    def get_new_color(self):
        # get current state coordinates
        x = self.maze_problem.current_state[0]
        y = self.maze_problem.current_state[1]

        # randomly choose movement to new state
        new_state = choice([[x+1,y],[x-1,y],[x,y+1],[x,y-1]])
        
        if not self.maze_problem.maze.is_floor(new_state[0],new_state[1]):
            new_state = self.maze_problem.current_state
        chosen_floor_color = self.maze_problem.maze.get_floor(new_state[0],new_state[1])
        other_colors = set(["R","G","B","Y"]).difference(set(chosen_floor_color))

        inverse_probability = (1-self.maze_problem.color_probability)/3
        p_distribution = [self.maze_problem.color_probability,inverse_probability,inverse_probability,inverse_probability]
        new_color = np.random.choice([chosen_floor_color]+list(other_colors),p=p_distribution)

        self.maze_problem.true_states += [new_state]
        self.maze_problem.observed_color += [new_color]
        
        return new_color

if __name__ == "__main__":

    test_maze1 = Maze("PA6/maze4.maz")
    problem = MazeProblem(test_maze1)
    solver = MarkovSolver(problem)
    
    solver.filtering()
    problem.show_solution()
    solver.viterbi()
