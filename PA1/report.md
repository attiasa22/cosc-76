### PA1 - Report
#### COSC 76 - 21F
##### Ariel Attias


(a) Description: How do your implemented algorithms work? What design decisions did you make? How you laid out the problems?

a. Description: 
  1. For **BFS** I followed the structure of the provided pseudocode. The frontier is implemented as a queue, and I used a dictionary (Python's hash table implementation) to store visited nodes to prevent looping. 
  
  Using a dictionary as opposed to a linked list is important to maintain O(1) run-time for detecting if a state is visited. I used a helper function to backchain the solution and to reuse the code for the other search strategies.

  2. For **DFS** I followed the structure of Recursive DFS presented in class.

  3. For **IDS** I reused the DFS code by just calling the DFS function in a for loop and increasing the depth by the for-loop counter.

  4. For the **FoxProblem** class, I defined `get_successors`,`check_successor_state`, and `goal_test`. `get_successors` creates all possible successor states by using a boolean based on the state of the boat. It either adds or subtracts a fox, a chicken, two foxes, two chickens, or one of both to create all 5 possible states, and then uses `check_successor_state` to return only the true successor states. `check_successor_state` creates the right bank state as well and checks that both banks follow the rule. This was implemented this way to be as clear as possible, reflect how humans think of the problem, and also allows the function to be reusable no matter the test case.

(b) Evaluation: Do your implemented algorithms actually work? How well? If it doesn’t work, can you tell why not? What partial successes did you have that deserve partial credit? Include a comparison of running time results using different heuristics and inference.

The algorithms actually work. Using Python's `timeit` library, I found the following"

| Problem      | Method     |Time (seconds)|
| ----------- | ----------- | ----------- |
| 331         | BFS         | 0.024742385 |
| -         | DFS         | 009722079   |
| -         | IDS         | 011253211   |
| 551         | BFS         | 0.022018086 |
| -         | DFS         | 0.009435617 |
| -         | IDS         | 0.965612073 |
| 541         | BFS         | 0.119463483 |
| -         | DFS         | 0.015895401 |
| -         | IDS         | 0.019852066 |

DFS performed in the least amount of time, while IDS followed closely behind except for when there is no solution, which makes sense as it is exhausting every path at every level before reaching the limit. BFS suffored from a similar issue by expanding into many useless paths, but did not perform as badly as IDS when there was no solution.

(c) Responses to discussion questions that are included within the points in "Required tasks" and the following point:

Discussion that needs to be in the report: States are either legal, or not legal.  First, give an upper bound on the number of states, without considering legality of states.  (Hint -- 331 is one state.  231 another, although illegal.  Keep counting.) Describe how you got this number.

Given  C chickens, there are C+1 amounts of chickens possible in a state (0,1,2,...,C). The same goes for foxes. 1 boat gives two options - the boat is either there or at the other bank. Therefore there are (C+1)(F+1)(2) possible states.

Does path-checking depth-first search save significant memory with respect to breadth-first search?  Draw an example of a graph where path-checking DFS takes much more run-time than breadth-first search; include in your report and discuss.

Yes, path-checking DFS saves significant memory with respect to BFS due to the lack of memoization.

<img width="744" alt="Screen Shot 2021-09-23 at 1 42 00 PM" src="https://user-images.githubusercontent.com/72452765/134557195-9c87bd10-8270-4fab-ba3a-0c3c6461e003.png">

In this example graph, a lexicographical search would yield a much longer Run-time for DFS, as it would have to traverse all the nodes before reaching goal X from start A. However, because X is so shallow, a BFS search would immediately find it.

Does memoizing DFS save significant memory with respect to breadth-first search?  Why or why not? As a reminder, there are two styles of depth-first search on a graph.  One style, memoizing keeps track of all states that have been visited in some sort of data structure, and makes sure the DFS never visits the same state twice. 

No it does not - memoizing DFS dramitically increases the space needed for DFS, as the frontier is much smaller than BFS. BFS's frontier is already big, so memoizing leads to space complexity not much larger than what it already is. Original DFS or DFS with path checking keeps a space complecity of O(bm) and O(m) respectively, where b is the branching factor of the tree and m is the longest path.

Discussion questions:  On a graph, would it make sense to use path-checking DFS, or would you prefer memoizing DFS in your iterative deepening search?  Consider both time and memory aspects.  (Hint.  If it's not better than BFS, just use BFS.)

On a graph, it would make sense to use path-checking DFS in order to maintain the low space complexity of O(bd). Whether or not path-checking or memoization is used, the time complexity is the same, O(b^d). If we switch to memoizing DFS, we are no better than BFS.

- Lossy chickens and foxes: Every fox knows the saying that you can't make an omelet without breaking a few eggs.  What if, in the service of their faith, some chickens were willing to be made into lunch?  Let us design a problem where no more than E chickens could be eaten, where E is some constant.  What would the state for this problem be?  What changes would you have to make to your code to implement a solution?  Give an upper bound on the number of possible states for this problem.  (You need not implement anything here.)

The state of this problem would be similar to the original problem, with the additional information of how many chickens the foxes have eaten. For example, state (2,2,1,1) describes a left bank with 2 chickens, 2 foxes, a boat, and one chicken eaten. I would need to change my `get_successors`,`check_successor_state`, and `goal_test` functions. `get_successors` would need to create the additional permutations of spaces where a chicken is eaten, as well as the other actions possible. `check_successor_state` would now need to allow some wiggle room based on E to determine if a space is actually a successor, most notably in a case where too many chickens will be eaten. Lastly, the `goal_test` function would need to account for the E possible end states (0,0,i,0): 0 <= i <= E.

Given C chickens, F foxes, E eaten chickens, and 1 boat, the total amount of possible states is (C+1) * (F+1) * (E+1) * 2.
