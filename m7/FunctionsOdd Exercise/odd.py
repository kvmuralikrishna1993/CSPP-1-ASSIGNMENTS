"""# Exercise: odd
# Write a Python function, odd, that takes in one number and returns True
when the number is odd and False otherwise.
# You should use the % (mod) operator, not if.
# This function takes in one number and returns a boolean."""


def odd(xi_):
    '''x: int or float.returns: True if x is odd, False otherwise'''
    return xi_%2 == 1
def main():
    """Main program starts here"""
    data_ = int(input())
    print(odd(int(data_)))
if __name__ == "__main__":
    main()
