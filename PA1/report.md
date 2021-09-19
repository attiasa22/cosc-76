### PA1 - Report
#### COSC 76 - 21F
##### Ariel Attias


(a) Description: How do your implemented algorithms work? What design decisions did you make? How you laid out the problems?

a. Description: 
  1. For **BFS** I followed the structure of the provided pseudocode. The frontier is implemented as a queue, and I used a dictionary (Python's hash table implementation) to store visited nodes to prevent looping. 
  
  Using a dictionary as opposed to a linked list is important to maintain O(1) run-time for detecting if a state is visited. I used a helper function to backchain the solution and to reuse the code for the other search strategies.

  2. For **DFS** I followed the structure of the provided pseudocode. The frontier is implemented as a stack, and I also used a dictionary to store visited nodes.

  3. For **IDS** I reused the DFS code by just calling the DFS function in a for loop and increasing the depth by the for-loop counter.

  4. For the **FoxProblem** class, I defined `get_successors`,`check_successor_state`, and `goal_test`. `get_successors` creates all possible successor states by using a boolean based on the state of the 


(b) Evaluation: Do your implemented algorithms actually work? How well? If it doesn’t work, can you tell why not? What partial successes did you have that deserve partial credit? Include a comparison of running time results using different heuristics and inference.
(c) Responses to discussion questions that are included within the points in "Required tasks" and the following point:
- Lossy chickens and foxes: Every fox knows the saying that you can't make an omelet without breaking a few eggs.  What if, in the service of their faith, some chickens were willing to be made into lunch?  Let us design a problem where no more than E chickens could be eaten, where E is some constant.  What would the state for this problem be?  What changes would you have to make to your code to implement a solution?  Give an upper bound on the number of possible states for this problem.  (You need not implement anything here.)

a README file with the instructions on how to execute the program.
Please write your report in Markdown in report.md. Then use pandoc or something similar to generate a pdf. (If you are having trouble with this step, just leave it in Markdown.) Include both files in your submission, as well as all figures (as pdf).
