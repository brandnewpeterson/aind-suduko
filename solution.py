import collections

assignments = []
rows = 'ABCDEFGHI'
cols = '123456789'

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [x+y for x in A for y in B]

boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
# Define diagonal units and include them in the list of units
diag_units = [[rows[i]+cols[i] for i in range(0, len(rows))], [rows[i]+list(cols)[::-1][i] for i in range(0, len(rows))]]
unitlist = row_units + column_units + square_units + diag_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    keys = cross(list(rows), list(cols))
    vals = [x if x is not '.' else '123456789' for x in grid]
    return dict(zip(keys, vals))

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

def eliminate(values):
    """
    Eliminate any single-digit possible values from multi-digit possible values within each unit.
    Args:
        values(dict): The sudoku in dictionary form
    Returns:
        the values dictionary with the single-digit possible values revoved from the multi-digit possible values within each unit.
    """
    # Loop over all values
    for key in values:
        if len(values[key]) == 1:
            # Note the key of positions with single values
            elim_num = values[key]
            # Loop over the peers of the position with the single value
            # and remove that value from two-digit and greater possible values
            for p in peers[key]:
                if len(values[p]) > 1:
                    values[p] = values[p].replace(elim_num, '')
    return values

def only_choice(values):
    """
    Determine if only one box in a unit would allow a certain digit. If so, assign box that digit.
    Args:
        values(dict): The sudoku in dictionary form
    Returns:
        the values dictionary with the single-digit values assigned as final values.
    """
    # Loop over all values
    for key in values:
        for unit in units[key]:
            # Concat possible unit values
            poss_unit_vals = ''
            for pos in unit:
                poss_unit_vals += values[pos]
            # Loop over unit and if it's corresponding possible value is only one digit long make the final value match
            for pos in unit:
                for digit in values[pos]:
                    if poss_unit_vals.count(digit) == 1:
                         values[pos] = digit
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Find all instances of naked twins and store them as a dictionary
    pairs = {}
    for key in units:
        for unit in units[key]:
            if key not in pairs.keys():
                pairs[key] = []
            twins = []
            for poss in unit:
            # Mark all twins
                if len(values[poss]) == 2:
                    twins.append(values[poss])
                #Keep only twins that exist as pairs per unit
            pairs[key].append([item for item, count in collections.Counter(twins).items() if count == 2 ])

    # Eliminate the naked twins as possibilities for peers in the same unit.
    for key in units:
        c = 0
        for unit in units[key]:
            for value in pairs[key][c]:
                for digit in list(value):
                    if values[key] != value and len(values[key])>1:
                        values[key] = values[key].replace(digit, '')
            c=c+1
    return values

def check_if_solved(values):
    """Check to see if the puzzle is solved.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        boolean indicating whether puzzle is solved for not.
    """
    solved = False
    vals_length = 0
    for key in values:
        vals_length += len(values[key])
    if vals_length == 81:
        solved = True
    return solved

def reduce_puzzle(values):
    """Remove invalid possible values from gameboard by utilizing eliminate, only choice, naked twins and search strategies.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with invalid possible values removed or a False boolean in the case that a valid interim solution cannot be found.
    """
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        # Use the Eliminate Strategy
        values = eliminate(values)
        if check_if_solved(values):
            break


        # Use the Only Choice Strategy
        values = only_choice(values)
        if check_if_solved(values):
            break

        # Use the Naked Twins Strategy
        values = naked_twins(values)
        if check_if_solved(values):
            break

        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            #print("sanity check failed")
            return False
    return values

def search(values):
    """After reducing possible values using multiple strategies, recursively search gameboard for positions with least number of possible values and try each of those values for a possible final solution.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the gameboard solution or a False boolean in the case that no solution can be found.
    """    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    # Choose one of the unfilled squares with the fewest possibilities
    # Find smallest set of possible vals
    if values is False:
        #print("search failed")
        return False ## Failed earlier
    if check_if_solved(values):
        return values ## Solved!

    # Find the postion with the smallest set of possible value.
    max = 9
    for key in values:
        if len(values[key]) < max and len(values[key]) > 1:
            max = len(values[key])
    for key in values:
        if len(values[key]) == max:
            smallest_set = values[key]
            smallest_key = key

    # Test each digit in that smallest set to see if it solves.
    for val in smallest_set:
        test_values = values.copy()
        test_values[smallest_key] = val
        test_values = search(test_values)
        if test_values:
            return test_values

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    values = grid_values(grid)
    return search(values)

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
