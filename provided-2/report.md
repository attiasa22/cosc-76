# PA3 - Chess
## Report
### by Ariel Attias for COSC 76 21F


(a) Description: How do your implemented algorithms work? What design decisions did you make?
   
  1. Minimax
  
  The Minimax application follows the pseudocode of the AI: A modern Approach very closely, and splits the recursive min and max functions of Minimax despite the reuse of code to maintain clarity.
  The cutoff test works by checking if the game is over, and then returns negative infinity if the Minimax player is checkmated, infinity if the Minimax player checkmates, and a heuristic that scores the difference in points derived from material otherwise.
  
  The heuristic uses the chess library to go through every piece and adds points if the material belongs to the Minimax player, and subtracts otherwise. The points values for the pieces are stored in a dictionary.
  
  2. AlphaBeta Pruning
  
  The Alpha Beta pruning follows the pseudocode and extends the implementation of Minimax. The heuristic and cutoff testing remains the same.
  
  3. Iterative Deepening 
  
  Iterative deepening takes either Minimax or AlphaBeta as a search method and increments the depth up to a certain number and returns the best move of all the best moves found at each depth.
  
 
  (b) Evaluation: Do your implemented algorithms actually work? How well? If it doesn’t work, can you tell why not? What partial successes did you have that deserve partial credit?
 
 (c) Responses to discussion questions that are included within the points in "The Task". Here the discussion questions are reported for ensuring that you found all of them:
     
1) (minimax and cutoff test) Vary maximum depth to get a feeling of the speed of the algorithm. Also, have the program print the number of calls it made to minimax as well as the maximum depth.  Record your observations in your document.
      
2) (evaluation function) Describe the evaluation function used and vary the allowed depth, and discuss in your document the results.
      
3) (alpha-beta) Record your observations on move-reordering in your document.
      
4) (iterative deepening) Verify that for some start states, best_move changes (and hopefully improves) as deeper levels are searched. Discuss the observations in your document.
