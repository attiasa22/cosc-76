from Maze import Maze
from time import sleep

class SensorlessProblem:

    ## You write the good stuff here:
    def __init__(self, maze):
        self.maze = maze
        self.start_state= tuple(self.initBeliefStates())
        self.height = maze.height

    def initBeliefStates(self):
        beliefStates =[]
        for i in range(self.maze.width):
            for j in range(self.maze.height):
                if self.maze.is_floor(i,j):
                    beliefStates+=(i,j)
        return beliefStates


    def get_successors(self, beliefStates):
        #go through the 4 possible directions
        northAction = self.check_successors(0 , 1, beliefStates)
        southAction = self.check_successors(0, -1, beliefStates)
        eastAction = self.check_successors(1, 0, beliefStates)
        westAction = self.check_successors(-1, 0, beliefStates)
        #check if the successor belief state 
        return [northAction] + [southAction] + [eastAction] + [westAction]

    def check_successors(self, xChange, yChange, beliefStates):
        visited=set()
        successors=[]
        #for each belief state
        #check if the successor belief state 
        for index in range(0,len(beliefStates),2):

            newX = beliefStates[index]+xChange
            newY = beliefStates[index+1]+yChange
            if self.maze.is_floor(newX,newY):
                successors+=(newX, newY)
                visited.add((newX,  newY))
            elif (beliefStates[index],  beliefStates[index+1]) not in visited:
                successors+=(beliefStates[index],  beliefStates[index+1])
                visited.add((beliefStates[index],  beliefStates[index+1]))
        return list(successors)

    def goal_test(self,beliefStates):
        if len(beliefStates)==2:
            return True
        return False 

    def heuristic_fn(self, successorStates):
        print(len(successorStates))
        return len(successorStates)

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


## A bit of test code

if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_problem = SensorlessProblem(test_maze3)

    print(test_problem.get_successors(test_problem.initBeliefStates()))
