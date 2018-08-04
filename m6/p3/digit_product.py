'''
Given a  number int_input, find the product of all the digits
example:input: 123
        output: 6'''
def main():
    '''Read any number from the input, store it in variable int_input.'''
    int_input = int(input())
    fl_ = 0
    if int_input < 0:
        int_input = abs(int_input)
        fl_ = 1
    mul_ = 1
    rem_ = 1
    str_ = str(int_input)
    for i in str_:
        rem_ = int(i)
        mul_ = mul_ * rem_
    if fl_ == 1:
        mul_ = -mul_
    print(mul_)
if __name__ == "__main__":
    main()
