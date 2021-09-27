from Maze import Maze
from time import sleep

class MazeworldProblem:

    ## you write the constructor, and whatever methods your astar function needs

    def __init__(self, maze, goal_locations):
        self.maze = maze
        self.goal_locations = goal_locations
        self.width = maze.width
        self.height = maze.height
        self.robotCount = len(self.maze.robotloc)//2

    def __str__(self):
        string =  "Mazeworld problem: "
        return string


        # given a sequence of states (including robot turn), modify the maze and print it out.
        #  (Be careful, this does modify the maze!)

    def get_successors(self, state):
        self.maze.robotloc=list(state[1:])

        robot = state[0]
        #indeces in tuple of coordinates
        xCoordinate = 2 * robot + 1
        yCoordinate = 2 * robot + 2
        
        #north 
        northState = list(state)
        northState[yCoordinate] += 1
        #south
        southState = list(state)
        southState[yCoordinate] -= 1
        #east
        eastState = list(state)
        eastState[xCoordinate] += 1
        #west
        westState = list(state)
        westState[xCoordinate] -= 1

        return self.check_successors(northState, xCoordinate, yCoordinate) + self.check_successors(southState,xCoordinate, yCoordinate) + self.check_successors(eastState, xCoordinate, yCoordinate) + self.check_successors(westState, xCoordinate, yCoordinate)

    def check_successors(self, state, xCoordinate,yCoordinate ):
        successors = []

        if self.maze.is_floor(state[xCoordinate],state[yCoordinate]) and not self.maze.has_robot(state[xCoordinate],state[yCoordinate]):
            
            
            for i in range(self.robotCount):
                newState =  list.copy(state)
                newState[0] = i
                successors += [newState]

        return successors

    def goal_test(self,locations):
        if locations==self.goal_state:
            return 1
        else:
            return 0

    def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robotloc = tuple(self.start_state[1:])

        for state in path:
            print(str(self))
            self.maze.robotloc = tuple(state[1:])
            sleep(1)

            print(str(self.maze))


## A bit of test code. You might want to add to it to verify that things
#  work as expected.

if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))
    '''
    ##.##
    #...#
    #.#.#
    #...#
    #...#
    #.###
    \robot 1 0
    \robot 1 1
    \robot 2 1
    '''
    print(test_mp.get_successors((0, 1, 0, 1, 2, 2, 1)))