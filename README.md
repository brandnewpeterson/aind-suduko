# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?
A: To quote from the lecture: "Constraint Propagation is all about using local constraints in a space . . . to dramatically reduce the search space. As we enforce each [local] constraint, we see how it introduces new constraints for other parts of the board . . . "

The naked twins strategy employs constraint propagation. Local constraints on a set of two boxes let us deduce additional constraints for the greater unit (the row, column, 3x3 grid, or diagonal in which the two boxes sit). Specifically, we first look for a box that has the local constraint of only two possible values. We then see if the unit has another box with that identical local constraint (the same two possible values). If we find such a set of "twins", we know that one of the twins must have one of the possible values, and the other twin must have the other possible value. Which twin has which possible value, we don't yet know, but we can deduce that neither of these two possible values can exist in the rest of the unit. We have thus propagated a local constraint on the twins to the rest of the unit. We can remove the twin's two possible values from the possible values of every other box within the unit.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: Constraint propagation within the context of sudoku means examining local constraints on a box or small set of boxes in order to deduce additional constraints for the rest of the gameboard.

Diagonal sudoku introduces two additional units to the gameboard: those formed by diagonally linking the corners of the gameboard. In practice this means that some boxes will have an extra unit's worth of peers. Boxes lying on the diagonals belong to four units (a row, column, 3x3 box, *and* one of the diagonals) instead of the three for the other boxes. This means that for each strategy we deploy to solve the gameboard, we can eliminate possible values from a greater number of peer boxes. The power of constraint propagation is thus magnified.

If we take as an example the elimination strategy, the test board we're given starts with a 2 in the top-right corner. As it's a single digit, this box is locally constrained to have a final value of two. We can then deduce that all of this box's peers (all other boxes within the four units it lies within) cannot have a 2 as a possible value. The additional diagonal unit to which the corner box belongs allows us to remove 2 as a possible value from the 8 additional boxes that lie within the left-slanting diagonal. Were diagonals not included, the elimination strategy would affect fewer peers (just the boxes within the rows, columns and 3x3 units).

Similarly, the naked twins strategy plays out within greater number of peers when we play diagonal sudoku versus regular sudoku.

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
