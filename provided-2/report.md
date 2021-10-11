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
 
 The implemented algorithms actually work. Alpha Beta pruning was tested by counting each node visited and improves significantly with respect to Minimax. In a similar game, these are the number of nodes visited at each depth.
 
 | Depth      | Minimax nodes visited| AlphaBeta nodes visited|
| ----------- | -------------------- | ---------------------- |
| 1         | 22         | 22 |
| 2         | 603         | 117   |
| 3         | 13,619         | 1023   |
| 4         | 388,425         | 5846 |

From a chess perspective, Alpha Beta performs better than Minimax. As the human player, I played the same moves and recorded them.

Alpha Beta 
<pre>
r n b q k b n r
p p p p p p p p
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
P P P P P P P P
R N B Q K B N R
----------------
a b c d e f g h

White to move

Please enter your move: 
d2d4
True
r n b q k b n r
p p p p p p p p
. . . . . . . .
. . . . . . . .
. . . P . . . .
. . . . . . . .
P P P . P P P P
R N B Q K B N R
----------------
a b c d e f g h

Black to move

4823
r n b q k b n r
p p p p . p p p
. . . . p . . .
. . . . . . . .
. . . P . . . .
. . . . . . . .
P P P . P P P P
R N B Q K B N R
----------------
a b c d e f g h

White to move

Please enter your move: 
e2e4
True
r n b q k b n r
p p p p . p p p
. . . . p . . .
. . . . . . . .
. . . P P . . .
. . . . . . . .
P P P . . P P P
R N B Q K B N R
----------------
a b c d e f g h

Black to move

10597
r n b q k b . r
p p p p . p p p
. . . . p . . n
. . . . . . . .
. . . P P . . .
. . . . . . . .
P P P . . P P P
R N B Q K B N R
----------------
a b c d e f g h

White to move

Please enter your move: 
b1c3
True
r n b q k b . r
p p p p . p p p
. . . . p . . n
. . . . . . . .
. . . P P . . .
. . N . . . . .
P P P . . P P P
R . B Q K B N R
----------------
a b c d e f g h

Black to move

20218
r n b q k . . r
p p p p . p p p
. . . . p . . n
. . . . . . . .
. b . P P . . .
. . N . . . . .
P P P . . P P P
R . B Q K B N R
----------------
a b c d e f g h

White to move

Please enter your move: 
a2a3
True
r n b q k . . r
p p p p . p p p
. . . . p . . n
. . . . . . . .
. b . P P . . .
P . N . . . . .
. P P . . P P P
R . B Q K B N R
----------------
a b c d e f g h

Black to move

31064
r n b q k . . r
p p p p . p p p
. . . . p . . n
. . . . . . . .
. . . P P . . .
P . b . . . . .
. P P . . P P P
R . B Q K B N R
----------------
a b c d e f g h

White to move

Please enter your move: 
b2c3
True
r n b q k . . r
p p p p . p p p
. . . . p . . n
. . . . . . . .
. . . P P . . .
P . P . . . . .
. . P . . P P P
R . B Q K B N R
----------------
a b c d e f g h

Black to move

40847
r n b q k r . .
p p p p . p p p
. . . . p . . n
. . . . . . . .
. . . P P . . .
P . P . . . . .
. . P . . P P P
R . B Q K B N R
----------------
a b c d e f g h

White to move

Please enter your move: 
g1f3
True
r n b q k r . .
p p p p . p p p
. . . . p . . n
. . . . . . . .
. . . P P . . .
P . P . . N . .
. . P . . P P P
R . B Q K B . R
----------------
a b c d e f g h

Black to move

50782
r n b q k r n .
p p p p . p p p
. . . . p . . .
. . . . . . . .
. . . P P . . .
P . P . . N . .
. . P . . P P P
R . B Q K B . R
----------------
a b c d e f g h

</pre>



Minimax

<pre>

Black to move

13016
r n b q k b . r
p p p p p p p p
. . . . . . . n
. . . . . . . .
. . . P . . . .
. . . . . . . .
P P P . P P P P
R N B Q K B N R
----------------
a b c d e f g h

White to move

Please enter your move: 
e2e4
True
r n b q k b . r
p p p p p p p p
. . . . . . . n
. . . . . . . .
. . . P P . . .
. . . . . . . .
P P P . . P P P
R N B Q K B N R
----------------
a b c d e f g h

Black to move

30616
r n b q k b r .
p p p p p p p p
. . . . . . . n
. . . . . . . .
. . . P P . . .
. . . . . . . .
P P P . . P P P
R N B Q K B N R
----------------
a b c d e f g h

White to move

Please enter your move: 
b1c3
True
r n b q k b r .
p p p p p p p p
. . . . . . . n
. . . . . . . .
. . . P P . . .
. . N . . . . .
P P P . . P P P
R . B Q K B N R
----------------
a b c d e f g h

Black to move

47391
r n b q k b . r
p p p p p p p p
. . . . . . . n
. . . . . . . .
. . . P P . . .
. . N . . . . .
P P P . . P P P
R . B Q K B N R
----------------
a b c d e f g h

White to move

Please enter your move: 
g1f3
True
r n b q k b . r
p p p p p p p p
. . . . . . . n
. . . . . . . .
. . . P P . . .
. . N . . N . .
P P P . . P P P
R . B Q K B . R
----------------
a b c d e f g h

Black to move

64543
r n b q k b . r
p p p p p p p p
. . . . . . . .
. . . . . . . .
. . . P P . n .
. . N . . N . .
P P P . . P P P
R . B Q K B . R
----------------
a b c d e f g h

White to move

Please enter your move: 
h2h3
True
r n b q k b . r
p p p p p p p p
. . . . . . . .
. . . . . . . .
. . . P P . n .
. . N . . N . P
P P P . . P P .
R . B Q K B . R
----------------
a b c d e f g h

Black to move

89791
r n b q k b . r
p p p p p p p p
. . . . . . . n
. . . . . . . .
. . . P P . . .
. . N . . N . P
P P P . . P P .
R . B Q K B . R
----------------
a b c d e f g h

White to move

Please enter your move: 
g2g4
True
r n b q k b . r
p p p p p p p p
. . . . . . . n
. . . . . . . .
. . . P P . P .
. . N . . N . P
P P P . . P . .
R . B Q K B . R
----------------
a b c d e f g h

Black to move

107367
r n b q k b r .
p p p p p p p p
. . . . . . . n
. . . . . . . .
. . . P P . P .
. . N . . N . P
P P P . . P . .
R . B Q K B . R
----------------
a b c d e f g h

White to move

Please enter your move: 
g4g5
True
r n b q k b r .
p p p p p p p p
. . . . . . . n
. . . . . . P .
. . . P P . . .
. . N . . N . P
P P P . . P . .
R . B Q K B . R
----------------
a b c d e f g h

Black to move

121535
r n b q k b . r
p p p p p p p p
. . . . . . . n
. . . . . . P .
. . . P P . . .
. . N . . N . P
P P P . . P . .
R . B Q K B . R
----------------
a b c d e f g h

White to move

Please enter your move: 
g5h6
True
r n b q k b . r
p p p p p p p p
. . . . . . . P
. . . . . . . .
. . . P P . . .
. . N . . N . P
P P P . . P . .
R . B Q K B . R
----------------
a b c d e f g h

Black to move

135484
r n b q k b . r
p p p p p p . p
. . . . . . . p
. . . . . . . .
. . . P P . . .
. . N . . N . P
P P P . . P . .
R . B Q K B . R
----------------
a b c d e f g h

White to move

Please enter your move: 
e4e5
True
r n b q k b . r
p p p p p p . p
. . . . . . . p
. . . . P . . .
. . . P . . . .
. . N . . N . P
P P P . . P . .
R . B Q K B . R
----------------
a b c d e f g h

Black to move

147196
r n b q k . . r
p p p p p p b p
. . . . . . . p
. . . . P . . .
. . . P . . . .
. . N . . N . P
P P P . . P . .
R . B Q K B . R
----------------
a b c d e f g h

White to move

Please enter your move: 
h8h7
  That is not a legal move!
Please enter your move: 
h1g1
True
r n b q k . . r
p p p p p p b p
. . . . . . . p
. . . . P . . .
. . . P . . . .
. . N . . N . P
P P P . . P . .
R . B Q K B R .
----------------
a b c d e f g h

Black to move

165534
r n b q k . r .
p p p p p p b p
. . . . . . . p
. . . . P . . .
. . . P . . . .
. . N . . N . P
P P P . . P . .
R . B Q K B R .
----------------
a b c d e f g h

</pre>

 (c) Responses to discussion questions that are included within the points in "The Task". Here the discussion questions are reported for ensuring that you found all of them:
     
1) (minimax and cutoff test) Vary maximum depth to get a feeling of the speed of the algorithm. Also, have the program print the number of calls it made to minimax as well as the maximum depth.  Record your observations in your document.

I have attached the count above, and minimax performs very slowly after increasing the depth to 4 or 5. The above text also has the number of calls attached.
      
2) (evaluation function) Describe the evaluation function used and vary the allowed depth, and discuss in your document the results.
      
The evaluation function used is a measure of the difference in material based on the typical scoring scheme (5 points for a rook, 3 points for a bishop or knight, etc.) The function works well enough in the opening game but is not enough for a full game which requires long-term strategy. For example, d2d4 is a drastically better first move than moving a knight, yet this evaluation function evaluates them to be the same, especially with not enough depth.
      
3) (alpha-beta) Record your observations on move-reordering in your document.

I sorted the list of legal moves with the line `moves.sort(key = lambda move: self.heuristic(board, move = move), reverse=True)` which sorts the moves in largest smallest points difference ('winning' to 'losing' positions).
      
4) (iterative deepening) Verify that for some start states, best_move changes (and hopefully improves) as deeper levels are searched. Discuss the observations in your document.
