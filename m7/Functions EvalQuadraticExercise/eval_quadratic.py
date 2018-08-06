'''# Exercise: eval quadratic # Write a Python function, evalQuadratic(a, b, c, x),
that returns the value of the quadratic a . x 2 + b . x + c
# This function takes in four numbers and returns a single number.'''
def evalquadratic_(ai_, bi_, ci_, xi_):
    '''Function starts here'''
    return ai_*xi_*xi_ + bi_*xi_ + ci_
def main():
    """Main program starts here"""
    data_ = input()
    data_ = data_.split(' ')
    data_ = list(map(float, data_))
    # print(data)
    as_ = len(data_)
    for val_ in range(as_):
        temp_ = str(data_[val_]).split('.')
        if temp_[1] == '0':
            data_[val_] = int(float(str(data_[val_])))
        else:
            data_[val_] = data_[val_]
    print(evalquadratic_(data_[0], data_[1], data_[2], data_[3]))

if __name__ == "__main__":
    main()
