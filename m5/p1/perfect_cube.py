'''# Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm
# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube
# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube'''

def main():
    '''# input is captured in s'''
    st_ = int(input())
    # watch out for the data type of value stored in s
    # your code starts here
    guess_ = 0
    flag = 0
    while guess_ < st_:
        if abs(guess_**3-st_) == 0:
            print(str(st_)+" is a perfect cube")
            flag = 1
            break
        else:
            guess_ = guess_+1
    if flag == 0:
        print(str(st_)+" is not a perfect cube")
if __name__ == "__main__":
    main()
