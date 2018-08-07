'''# Exercise: PowerRitr
# Write a Python function, recurPower(base, exp),
that takes in two numbers and returns the base^(exp) of given base and exp.
# This function takes in two numbers and returns one number.'''
def poweritr(base_, exp_):
    '''base: int or float.exp: int >= 0returns: int or float, base^exp'''
    res_ = 1
    while exp_ > 0:
        res_ = res_*base_
        exp_ = exp_-1
    return res_
def main():
    '''Main program starts here'''
    data_ = input()
    data_ = data_.split(' ')
    print(poweritr(float(data_[0]), int(data_[1])))
if __name__ == "__main__":
    main()
