# PA4 - Report
## COSC 76 - 21F
### Ariel Attias


**(a) Description: How do your implemented algorithms work? What design decisions did you make? How you laid out the problems?**

For code clarity, I split my code into the the following classes and/or files: 

`test_constraint_problem.py` is the high level access point for users  interacting or running the code on a Map Coloring or Circuit Board problem of interest. It uses the `MapColoring`, `SearchProblem`, and `CircuitBoardFitting` classes to solve problems the user has created. Here, the user also decides if they would like to solve the csp with heuristics and/or inferencing. Please read `readme.md` for more details on how to run the software.

`MapColoring.py` takes in a map as a constraint graph and the number of colors the users would like to use. This csp is solved with the variables being the locations and the values represent the colors. For ease of solving, *n* colors are represented as numbers 1 through *n*. All the Map Coloring class needs to do to ensure that the general CSP solver can solve the Map Coloring problem is have its own constraint check and set up the domain.



**(b) Evaluation: Do your implemented algorithms actually work? How well? If it doesn’t work, can you tell why not? What partial successes did you have that deserve partial credit? Include a comparison of running time results using different heuristics and inference.**

**(c) Responses to discussion questions that are included within the points in "Required tasks".**