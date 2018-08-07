'''# Exercise: Assignment-1
# Write a Python function, factorial(n),
that takes in one number and returns the factorial of given number.
# This function takes in one number and returns one number.'''
def factorial(num_):
    '''n is positive Integerreturns:
    a positive integer, the factorial of n.'''
    if num_ == 0:
        return 1
    return num_*factorial(num_-1)
def main():
    """Main program starts here"""
    value_ = input()
    print(factorial(int(value_)))
if __name__ == "__main__":
    main()
