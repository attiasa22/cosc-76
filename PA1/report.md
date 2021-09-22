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

The implemented algorithms actually work. All three functions return the correct answer in all three situations. Using Python's `timeit` library, I found

| Problem      | Method     |Time (seconds)|
| ----------- | ----------- | ----------- |
| 331         | BFS         | 0.024742385 |
| 331         | DFS         | 009722079   |
| 331         | IDS         | 011253211   |
| 551         | BFS         | 0.022018086 |
| 551         | DFS         | 0.009435617 |
| 551         | IDS         | 0.965612073 |
| 541         | BFS         | 0.119463483 |
| 541         | DFS         | 0.015895401 |
| 541         | IDS         | 0.019852066 |

(c) Responses to discussion questions that are included within the points in "Required tasks" and the following point:
- Lossy chickens and foxes: Every fox knows the saying that you can't make an omelet without breaking a few eggs.  What if, in the service of their faith, some chickens were willing to be made into lunch?  Let us design a problem where no more than E chickens could be eaten, where E is some constant.  What would the state for this problem be?  What changes would you have to make to your code to implement a solution?  Give an upper bound on the number of possible states for this problem.  (You need not implement anything here.)
