'''# Exercise: Assignment-2
# Write a Python function, sumofdigits,
that takes in one number and returns the sum of digits of given number.
# This function takes in one number and returns one number.'''
def sumofdigits_(num_):
    '''n is positive Integerreturns:
    a positive integer,the sum of digits of n.'''
    if num_ == 0:
        return 0
    return num_%10 + sumofdigits_(num_//10)
def main():
    '''Main function starts here'''
    value_ = input()
    print(sumofdigits_(int(value_)))
if __name__ == "__main__":
    main()
