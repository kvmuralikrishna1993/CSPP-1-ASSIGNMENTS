'''# Exercise: Is In
# Write a Python function, isIn(char, aStr),
that takes in two arguments a character and String and returns the isIn(char,
aStr) which retuns a boolean value.
# This function takes in two arguments character and
String and returns one boolean value.'''
def isin_(char_, str_):
    '''char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise'''
    len_ = len(str_)
    if len_ == 0:
        return False
    if len_ == 1:
        return str_ == char_
    if str_[len_//2] == char_:
        return True
    if str_[len_//2] > char_:
        return isin_(char_, str_[0:len_//2])
    return isin_(char_, str_[len_:]//2)
def main():
    '''Main function starts from here'''
    data_ = input()
    data_ = data_.split()
    print(isin_((data_[0][0]), data_[1]))


if __name__ == "__main__":
    main()
