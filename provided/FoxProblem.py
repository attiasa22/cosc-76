class FoxProblem:
    def __init__(self, start_state=(3, 3, 1)):
        self.start_state = start_state
        self.goal_state = (0, 0, 0)
        # you might want to add other things to the problem,
        #  like the total number of chickens (which you can figure out
        #  based on start_state
        self.total_chickens = start_state[0]

    # get successor states for the given state
    def get_successors(self, state):
        # you write this part. I also had a helper function
        # that tested if states were safe before adding to successor list
        successor_states = []
        boatPresence = 1
        # if the boat is present, the starting bank loses animals,
        if state[2]:
            boatPresence =- 1
        # if the boat is absent, the starting bank gain animals.
        else:
            boatPresence = 1
        # given a state, to get to the next state, either:
        # one chicken uses the boat
        chickenBoat = self.check_successor_state((state[0] + boatPresence,state[1],1-state[2]))
        # one fox uses the boat
        foxBoat = self.check_successor_state((state[0],state[1]+boatPresence,1- state[2]))
        # two chickens use the boat
        chickensBoat = self.check_successor_state((state[0] + boatPresence * 2,state[1],1-state[2]))
        # two foxes use the boat
        foxesBoat = self.check_successor_state((state[0],state[1]+boatPresence * 2,1- state[2]))
        # one chicken and one fox use the boat
        zooBoat = self.check_successor_state((state[0] + boatPresence,state[1]+boatPresence,1- state[2]))

        # return valid successor states
        return chickenBoat+foxBoat+chickensBoat+foxesBoat+zooBoat

    def check_successor_state(self,state):
        rightBankState=(self.total_chickens-state[0],self.total_chickens-state[1],1-state[2])
        # if there is a negative number of animals or boats
        if state[0]<0 or state[1]<0 or state[2]<0:
            return []
        # Left Bank: if there are more foxes than chickens
        elif state[0]<state[1] and state[0]>0:
            return []
        #Right Bank: if there are more foxes than chickens
        elif rightBankState[0]<rightBankState[1] and rightBankState[0]>0:
            return []
        else:
            return [state]
    # I also had a goal test method. You should write one.
    def goal_test(self,state):
        if state==self.goal_state:
            return 1
        else:
            return 0

    def __str__(self):
        string =  "Chickens and foxes problem: " + str(self.start_state)
        return string


## A bit of test code

if __name__ == "__main__":
    test_cp = FoxProblem((5, 5, 1))
    print(test_cp.get_successors((5, 5, 1)))
    print(test_cp)
