# PA5 - ReadMe
## COSC 76
### Ariel Attias




**A. Description: How do your implemented algorithms work? What design decisions did you make? How you laid out the problems?**

1. I started with GSAT, and followed the pseudocode exactly to ensure correctness. I first created a function to read the cnf and create a dictionary which takes in the line and convertes the line, for example "123" into a key value pair 123:1. The line "-123" would lead to key value pair 123:0, designating a false variable. <p> Determining if an assignment *T* (implemented as a dictionary)satisfies the clauses is done with `satisfies(T, clauses)` which goes through each clause adetermines whether the or statement is true or false. <p> If the random variable cross a certain threshold value, a random variable is flipped with the statement `T[p] = (T[p] + 1) % 2`. The modulus operator is used for correctness and clarity. <p> Otherwise, `find_p(T, clauses, variables)` is called to find our variable of interest *p*. The function goes through each variable and stores those with the greatest scores, where each true clause the variable flip fulfills increases the score by 1. From these variables (all tied for the best score), a random one is chosen. The function only returns *p* in order to maintain clarity and resemble the pseudocode. If a correct assignment *T* is found, it is written to a .sol file as described in the assignment.

2. Walksat follows the pseudocode as well. The main difference is that it used the function `find_unsatisfied_clauses(self, T, clauses)` to determine if assignment *T* satisfies the clauses and if not, returns the list of unsatisfied clauses as well. From these clauses, a random one is chosen and its variables are those Walksat will modify. <p>If the random variable crosses a threshold, one of these variables is randomly chosen and flipped.<p> Otherwise, `find_p(self, T, clauses, variables)` goes through the variables from the selected clause and finds the best one based on the described score.


**B. Evaluation: Do your implemented algorithms actually work? How well? If it doesn’t work, can you tell why not? What partial successes did you have that deserve partial credit?** 

Yes, both actually work as described, and worked for all the test cases. The solutions found are below.

|  Test Case | GSAT Solution| GSAT Number of Flips |WALKSAT Solution     |  WALKSAT Number of Flips|
| ----------- | ----------- | ----------- | ----------- | ----------- |
| One Cell    | A1          | 20          | B1          |  4          |
| All cells   |  A2         | 351         | B2          | 281         |
| Rows        |  A3         | ----------- | B3          | 417         |
|Rows and Cols|             | ----------- | B4          | 1763        |
| Rules       |             | ----------- | B5          | 1775        |
| Puzzle 1    |             | ----------- | B6          | 25979       |
| Puzzle 2    |             | ----------- | B7          | 43897       |
| Puzzle Bonus|             | ----------- | B8          | 24677       |
    
    A1
    1 0 0 | 0 0 0 | 0 0 0 
    0 0 0 | 0 0 0 | 0 0 0 
    0 0 0 | 0 0 0 | 0 0 0 
    ---------------------
    0 0 0 | 0 0 0 | 0 0 0 
    0 0 0 | 0 0 0 | 0 0 0 
    0 0 0 | 0 0 0 | 0 0 0 
    ---------------------
    0 0 0 | 0 0 0 | 0 0 0 
    0 0 0 | 0 0 0 | 0 0 0 
    0 0 0 | 0 0 0 | 0 0 0 
    A2
    4 1 4 | 3 2 7 | 1 7 6 
    2 9 7 | 7 3 6 | 9 6 1 
    4 5 4 | 2 9 1 | 4 5 4 
    ---------------------
    7 1 1 | 2 9 7 | 5 8 8 
    7 8 6 | 3 7 8 | 8 3 2 
    7 3 8 | 1 8 9 | 9 7 2 
    ---------------------
    6 7 9 | 3 7 9 | 3 5 9 
    2 3 7 | 4 3 4 | 1 8 7 
    3 9 3 | 6 6 4 | 2 7 6 

    B1
    7 0 0 | 0 0 0 | 0 0 0 
    0 0 0 | 0 0 0 | 0 0 0 
    0 0 0 | 0 0 0 | 0 0 0 
    -------------- ------
    0 0 0 | 0 0 0 | 0 0 0 
    0 0 0 | 0 0 0 | 0 0 0 
    0 0 0 | 0 0 0 | 0 0 0 
    ---------------------
    0 0 0 | 0 0 0 | 0 0 0 
    0 0 0 | 0 0 0 | 0 0 0 
    0 0 0 | 0 0 0 | 0 0 0

    B2
    9 5 1 | 3 8 6 | 6 2 5 
    6 3 9 | 7 4 2 | 2 8 9 
    7 9 8 | 9 1 1 | 4 1 3 
    ---------------------
    4 7 2 | 5 9 2 | 8 5 3 
    6 6 4 | 6 2 3 | 6 1 4 
    2 8 5 | 6 4 2 | 8 2 5 
    ---------------------
    7 6 8 | 7 1 4 | 6 4 7 
    9 4 9 | 9 3 2 | 9 1 9 
    9 3 4 | 3 4 7 | 6 3 7 

    B3
    5 8 9 | 7 1 6 | 4 2 3 
    7 8 1 | 2 3 5 | 6 9 4 
    3 5 9 | 4 2 7 | 1 6 8 
    ---------------------
    5 2 3 | 8 6 1 | 9 4 7 
    1 5 3 | 4 6 8 | 9 7 2 
    3 7 4 | 6 5 8 | 9 2 1 
    ---------------------
    2 4 6 | 7 9 3 | 8 1 5 
    9 3 7 | 8 5 2 | 4 6 1 
    9 5 1 | 4 7 8 | 6 3 2 

    B4
    6 5 3 | 4 8 9 | 2 7 1 
    2 6 8 | 5 3 7 | 9 1 4 
    9 4 5 | 8 1 6 | 3 2 7 
    ---------------------
    7 3 4 | 9 5 2 | 1 6 8 
    3 8 2 | 7 6 1 | 4 9 5 
    1 9 6 | 2 4 8 | 7 5 3 
    ---------------------
    8 1 9 | 6 7 3 | 5 4 2 
    4 7 1 | 3 2 5 | 6 8 9 
    5 2 7 | 1 9 4 | 8 3 6 

    B5
    3 1 2 | 7 4 9 | 6 8 5 
    9 5 4 | 1 8 6 | 3 7 2 
    7 6 8 | 2 5 3 | 1 4 9 
    ---------------------
    5 2 6 | 9 3 7 | 8 1 4 
    8 3 7 | 4 2 1 | 5 9 6 
    4 9 1 | 8 6 5 | 2 3 7 
    ---------------------
    6 4 5 | 3 7 8 | 9 2 1 
    1 7 3 | 6 9 2 | 4 5 8 
    2 8 9 | 5 1 4 | 7 6 3 

    B6
    5 9 4 | 3 8 6 | 1 2 7 
    3 7 6 | 2 9 1 | 8 5 4 
    2 8 1 | 4 5 7 | 3 6 9 
    ---------------------
    8 1 3 | 9 6 5 | 4 7 2 
    4 6 5 | 8 7 2 | 9 1 3 
    7 2 9 | 1 3 4 | 5 8 6 
    ---------------------
    6 5 8 | 7 4 3 | 2 9 1 
    9 4 2 | 6 1 8 | 7 3 5 
    1 3 7 | 5 2 9 | 6 4 8 

    B7 
    2 3 8 | 9 5 6 | 7 4 1 
    6 7 4 | 1 3 8 | 5 9 2 
    1 9 5 | 2 7 4 | 3 6 8 
    ---------------------
    8 5 9 | 7 6 1 | 4 2 3 
    3 4 6 | 8 2 5 | 1 7 9 
    7 1 2 | 4 9 3 | 8 5 6 
    ---------------------
    9 8 1 | 5 4 2 | 6 3 7 
    4 6 7 | 3 8 9 | 2 1 5 
    5 2 3 | 6 1 7 | 9 8 4 

    B8 
    5 3 4 | 6 7 8 | 9 1 2 
    6 7 2 | 1 9 5 | 3 4 8 
    1 9 8 | 3 4 2 | 5 6 7 
    ---------------------
    8 5 9 | 7 6 1 | 4 2 3 
    4 2 6 | 8 5 3 | 7 9 1 
    7 1 3 | 9 2 4 | 8 5 6 
    ---------------------
    9 6 1 | 5 3 7 | 2 8 4 
    2 8 7 | 4 1 9 | 6 3 5 
    3 4 5 | 2 8 6 | 1 7 9 