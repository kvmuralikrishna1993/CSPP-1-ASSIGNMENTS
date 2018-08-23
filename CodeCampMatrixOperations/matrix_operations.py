'''Matrix addition and Multiplication'''
def mult_matrix(m1_, order1, m2_, order2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if order1[1] != order2[0]:
        print("Error: Matrix shapes invalid for mult")
        return None
    result = []
    row = len(m1_)
    col = len(m2_[0])
    row2 = len(m2_)
    for i in range(row):
        temp = []
        for j in range(col):
            res = 0
            for k in range(row2):
                res += m1_[i][k]*m2_[k][j]
            temp.append(res)
        result.append(temp)
    return result

def add_matrix(m1_, order1, m2_, order2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if order1 != order2:
        print("Error: Matrix shapes invalid for addition")
        return None
    result = []
    for i, j in zip(m1_, m2_):
        res = []
        for k, v in zip(i, j):
            res.append(k+v)
        result.append(res)
    return result
def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    order = list(map(int, input().split(',')))
    temp2 = []
    for i in range(order[0]):
        temp = []
        temp = input().split(' ')
        if len(temp) != order[1]:
            print("Error: Invalid input for the matrix")
            return
        temp2.append(temp)
    matrix = [list(map(int, v)) for i, v in enumerate(temp2)]
    return [matrix, order]
def main():
    '''Main starts here'''
    # read matrix 1p
    matrix1 = read_matrix()
    matrix2 = read_matrix()
    if (matrix1 is None or matrix2 is None):
        return
    # read matrix 2

    # add matrix 1 and matrix 2
    print(add_matrix(matrix1[0], matrix1[1], matrix2[0], matrix2[1]))
    print(mult_matrix(matrix1[0], matrix1[1], matrix2[0], matrix2[1]))

    # multiply matrix 1 and matrix 2

if __name__ == '__main__':
    main()
