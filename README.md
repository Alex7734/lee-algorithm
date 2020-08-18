# Lee Algorithm Python --- BFS

1 Copy repository locally via ZIP

2 Run lee_algo.py

Dependencies needed: python, Tkinter(standard library)

PSEUDOCOD:
- Select start point, mark with 0 ( i := 0 )
- REPEAT
     Mark all unlabeled neighbors of points marked with i with i+1
     i := i+1
   UNTIL ((target reached) or (no points can be marked))
 - GO TO the target point
   REPEAT
     go to next node that has a lower mark than the current node
     add this node to path
   UNTIL (start point reached)