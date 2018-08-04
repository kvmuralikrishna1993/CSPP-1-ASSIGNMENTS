'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    str_ = input()
    emp = ''
    fl_ = 0
    for i in range(len(str_)):
        if str_[i] == '!' or str_[i] == '@' or str_[i] == '#':
            fl_ = 1
        elif str_[i] == '$' or str_[i] == '%' or str_[i] == '^' or str_[i] == '&' or str_[i] == '*':
            fl_ = 1
        if fl_ == 1:
            emp = emp+' '
        else:
            emp = emp+str_[i]
        fl_ = 0
    print(emp)

if __name__ == "__main__":
    main()
