'''# Exercise: fourth power
# Write a Python function, fourthPower,
that takes in one number and returns that value raised to the fourth power
# You should use the square procedure that you defined in
an earlier exercise exercise (you don't need to redefine square in this box;
# This function takes in one number and returns one number.'''
def square_(xi_):
    '''x: int or float.'''
    xi_ = xi_**2
    return xi_
def fourthpower_(xi_):
    '''x: int or float.'''
    return square_(square_(xi_))
def main():
    '''Main program starts here '''
    data_ = input()
    data_ = float(data_)
    temp_ = str(data_).split('.')
    if temp_[1] == '0':
        print(fourthpower_(int(float(str(data_)))))
    else:
        print(fourthpower_(data_))

if __name__ == "__main__":
    main()
