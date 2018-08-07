'''GCD using iteration'''
def gcditer_(num1_, num2_):
    '''a, b: positive integersreturns:
    a positive integer, the greatest common divisor of a & b.'''
    rem_num = num1_%num2_
    while num2_ != 0:
        if num1_%num2_ == 0:
            return num2_
        rem_num = num1_%num2_
        num1_ = num2_
        num2_ = rem_num
def main():
    '''Main function.'''
    data = input()
    data = data.split()
    print(gcditer_(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
