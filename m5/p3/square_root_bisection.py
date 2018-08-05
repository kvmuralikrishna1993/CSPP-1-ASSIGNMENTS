'''# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991'''

def main():
    '''Program starts here'''
    sq_ = float(input())
    epsilon_ = 0.01
    low_ = 0.0
    high_ = sq_
    ans_ = (high_+low_)/2.0
    while abs(ans_**2-sq_) >= epsilon_:
        if ans_**2 > sq_:
            high_ = ans_
        else:
            low_ = ans_
        ans_ = (high_+low_)/2.0
    print(ans_)
if __name__ == "__main__":
    main()
