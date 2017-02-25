# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: "Constraint propagation" in the context of suduko merely means that we employ reasoning about the rules of the game to eliminate possible values from each position on the gameboard. In the case of the "naked twins" strategy, we look for units (rows, columns, 3x3 boxes, and diagonals), that have two boxes with identical two-digit possible values. We can then reason that one of these boxes must have one of the values in the identical pair and the other box must have the remaining value. Thus, all other boxes in the unit will not have either of these values, and we can eliminate both values from their possible values.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: Again, "constraint propagation" in the context of Suduko merely means that we employ reasoning about the rules of the game to eliminate possible values from each position on the gameboard. With diagonal suduko, we introduce an additional constraint on possible values by saying that the two diagonal lines formed by the boxes that connect the four corners of the gameboard also constitute units. This means that certain positions fall into 4 units rather than just 3 (all the boxes in its same row, column, 3x3 box, *and*, if applicable, diagonal). As these units have overlapping boxes and as each unit must have only one value in the set {1...9}, the number of possible values is further reduced.

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project.
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.
