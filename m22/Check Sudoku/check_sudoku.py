'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''
import itertools

def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    if check_row(sudoku):
        if check_col(sudoku):
            if check_mini(sudoku):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
def check_row(sudoku):
    sudoku1 = []
    try:
        sudoku1 = [list(map(int, v)) for i, v in enumerate(sudoku)]
    except:
        len_ = 0
    count = 0
    for i in sudoku1:
        len_ = len(set(i))
        sum_ = sum(i)
        if len_ == 9 and sum_ == 45:
            count += 1
    if count == 9:
        return True
    return False

def transpose(sudoku):
    '''transpose'''
    transpose_ = []
    for i in range(len(sudoku)):
        row = []
        for j in range(len(sudoku[0])):
            row.append(sudoku[j][i])
        transpose_.append(row)
    return check_row(transpose_)

def check_col(sudoku):
    '''check column'''
    tsudoku = transpose(sudoku)
    return check_row(tsudoku)

def create_mini(sudoku):
    squares = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = []
            square = list(itertools.chain(row[j:j+3] for row in sudoku[i:i+3]))
            squares.append(square)
    new = []
    for i in squares:
        new.append([list(map(int, v)) for i, v in enumerate(i)])
    return new

def check_mini(sudoku):
    '''check mini'''
    squares = create_mini(sudoku)
    sort_squares = []
    for i in squares:
        temp = []
        for j in i:
            temp.extend(j)
        sort_squares.append(temp)
    count = 0
    for i in sort_squares:
        len_ = len(set(i))
        sum_ = sum(i)
        if len_ == 9 and sum_ == 45:
            count += 1
    if count == 9:
        return True
    return False

def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for i in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()
