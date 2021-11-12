import numpy as np
from sklearn.preprocessing import normalize
from MazeProblem import MazeProblem
from Maze import Maze
import timeit
import matplotlib.pyplot as plt

class MarkovSolver:

    def __init__(self, problem):
        self.problem = problem

    def filtering(self, observations):
        # this function continuously applies the matrix transformation version
        # f_1:t+1 = a(O_t+1)(T_transpose)(f_1:t)
        f_t = self.problem.initial_distribution
        transition_matrix_transpose = self.transition_matrix().T
        # apply the HMM a certain number of times
        for i in range(observations):
            observation_matrix = self.observation_matrix()
            # sci_kit learn's normalize function performs the same action as a in the equation
            f_t = normalize(((observation_matrix @ transition_matrix_transpose) @ f_t).reshape(-1,1), axis=0, norm = 'l1')
            self.problem.solution += [f_t]
        
    def viterbi(self):
        obvservation_space = self.problem.observation_space

        observations =  self.problem.observations
        transition_matrix = self.transition_matrix()
        emission_matrix = self.emission_matrix(obvservation_space)
        initial_probabilities = self.problem.initial_distribution
        
        state_size = len(self.problem.states)
        observation_count = len(observations)

        T1 = np.zeros((state_size, observation_count))
        T2 = np.zeros((state_size, observation_count))
        T1[:, 0] = initial_probabilities * emission_matrix[:, obvservation_space[observations[0]]]

        for i in range(1, observation_count):
            T1[:,i] = np.max((T1[:, i-1] * transition_matrix.T) * emission_matrix[:, obvservation_space[observations[i]]].T, 1)
            T2[:, i] = np.argmax(T1[:, i-1 ] * transition_matrix.T, 1)

        solution = np.zeros(observation_count)
        solution[-1] = np.argmax(T1[:, observation_count - 1])

        for i in reversed(range(1,observation_count )):
            solution[i - 1] = int(T2[int(solution[i]), i])

        self.problem.veterbi_solution = solution
        return solution

    # Given S possible states, an S x S matrix T is created, such that T[i][j] is chance that we go from i to j
    # Since our robot takes a random movement in the 4 cardinal directions, that chance is 0.25
    # However, a floor bordering a wall actually has a chance to come from itself, 
    # So any wall encountered is actually an increase of 0.25 to T[i][i]
    def transition_matrix(self):
        # initialize a S xS matrix of zeros
        dimension = len(self.problem.states)
        transition_matrix= np.zeros((dimension,dimension))
        # for each state
        for floor in self.problem.states:
            index = self.problem.states.index(floor)
            x = floor[0] 
            y = floor[1]
            # determine if neighboring cells are possible previous states
            self.set_matrix(transition_matrix, index, x+1, y)
            self.set_matrix(transition_matrix, index, x-1, y)
            self.set_matrix(transition_matrix, index, x, y+1)
            self.set_matrix(transition_matrix, index, x, y-1)

        return transition_matrix

    def set_matrix(self, transition_matrix, index_1, x, y):
        # if the cell is a state
        if [x,y] in self.problem.states:
                # set T[i][j] to probabilty of transition
                index_2 = self.problem.states.index([x,y])
                transition_matrix[index_2][index_1] = 0.25
        else:
            # if the cell is not a state
            # the movement will leave the robot in the same state
            # meaning that the state is reachable from itself
            transition_matrix[index_1][index_1] += 0.25

    # Create a diagonal S x S matrix 
    # where the diagonal values are the odds of that state occuring 
    # given a random movement event
    def observation_matrix(self):
        # initialize a 1 x S matrix
        # where each cell i is an observation probability of state i
        odds = [0]* len(self.problem.states)
        
        new_observation = self.problem.get_new_state()
        # for each state
        for index in range(len(self.problem.states)):
            # if state is the same as the observed state
            x = self.problem.states[index][0]
            y = self.problem.states[index][1]
            if self.problem.maze.get_floor(x, y) == new_observation:
                # add the probability it will be sensed correctly
                odds[index] = self.problem.color_probability
            else:
                odds[index] = 1 - self.problem.color_probability

        # O matrix is the S x S matrix whose diagonals are the observation probabilities
        observational_matrix = np.diag(odds)

        return observational_matrix

    def emission_matrix(self, obvservation_space):
        emission_matrix = np.full((len(self.problem.states), len(self.problem.observation_space)), self.problem.color_probability-1)

        for i in range((len(self.problem.states))):
            x = self.problem.states[i][0]
            y = self.problem.states[i][1]
            j = obvservation_space[self.problem.maze.get_floor(x,y)]
            emission_matrix[i, j] = self.problem.color_probability

        return emission_matrix

if __name__ == "__main__":
    
    test_maze1 = Maze("PA6/maze1.maz")
    problem = MazeProblem(test_maze1, 0.88)
    solver = MarkovSolver(problem)
    
    #solver.filtering(10)
    # uncomment for viterbi
    #print(solver.viterbi())
    #problem.show_solution()

    solver.filtering(20)
    a=(timeit.timeit('solver.viterbi()', "from __main__ import solver", number=5))
    solver.filtering(200)
    b=(timeit.timeit('solver.viterbi()', "from __main__ import solver", number=5))
    solver.filtering(2000)
    c=(timeit.timeit('solver.viterbi()', "from __main__ import solver", number=5))
    print(1)
    solver.filtering(20000)
    d=(timeit.timeit('solver.viterbi()', "from __main__ import solver", number=5))
    print(2)
    time_4_4 = [a,b,c,d]
    
    test_maze1 = Maze("PA6/maze4.maz")
    problem = MazeProblem(test_maze1, 0.88)
    solver = MarkovSolver(problem)
    
    #solver.filtering(20)
    # uncomment for viterbi
    # solver.viterbi()
    #problem.show_solution()

    solver.filtering(20)
    a=(timeit.timeit('solver.viterbi()', "from __main__ import solver", number=5))
    solver.filtering(200)
    b=(timeit.timeit('solver.viterbi()', "from __main__ import solver", number=5))
    solver.filtering(2000)
    c=(timeit.timeit('solver.viterbi()', "from __main__ import solver", number=5))
    print(1)
    solver.filtering(20000)
    d=(timeit.timeit('solver.viterbi()', "from __main__ import solver", number=5))
    print(4)
    time_2_2 = [a,b,c,d]
    print(time_2_2)
    


    plt.plot([20,200,2000, 20000],time_2_2, color = "green")
    plt.plot([20,200,2000, 20000],time_4_4, color = "red")
    plt.ylabel('Time (s)')
    plt.xlabel('filter calls')
    plt.legend(["2x2 maze", "4x4 maze",])
    plt.show()
    
    