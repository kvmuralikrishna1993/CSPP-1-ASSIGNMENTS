'''GCD using recursion.'''
def gcdrecr_(num1_, num2_):
    '''a, b: positive integersreturns:
    a positive integer, the greatest common divisor of a & b.'''
    rem_1 = 0
    if num1_%num2_ == 0:
        return num2_
    rem_1 = num1_%num2_
    num1_ = num2_
    num2_ = rem_1
    return gcdrecr_(num1_, num2_)
def main():
    '''main program starts here'''
    data = input()
    data = data.split()
    print(gcdrecr_(int(data[0]), int(data[1])))
if __name__ == "__main__":
    main()
