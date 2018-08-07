'''# Exercise: power_recur
# Write a Python function, power_recur(base, exp), that takes in two numbers
and returns the base^(exp) of given base and exp.
# This function takes in two numbers and returns one number.'''
def power_recur(base_, exp_):
    '''base: int or float.
    exp: int >= 0
    returns: int or float, base^exp'''
    if exp_ == 0:
        return 1
    return base_*power_recur(base_, exp_-1)
def main():
    '''Main program starts here'''
    data_ = input()
    data_ = data_.split(' ')
    print(power_recur(float(data_[0]), int(data_[1])))
if __name__ == "__main__":
    main()
