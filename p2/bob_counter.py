'''Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2'''

def main():
    '''Program starts here'''
    st_ = input()
    count_ = 0
    for i in range(0, len(st_)-1, 1):
        if (st_[i] == 'b' and st_[i+1] == 'o' and st_[i+2] == 'b'):
            count_ = count_+1
    print(count_)
if __name__ == "__main__":
    main()
