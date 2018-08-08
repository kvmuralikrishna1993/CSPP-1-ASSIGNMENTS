'''#Exercise : Function and Objects Exercise-1
#Implement a function that
converts the given testList = [1, -4, 8, -9] into [1, 4, 8, 9]'''
def apply_to_each(list1_, fun_):
    '''Function starts here'''
    len_ = len(list1_)
    intial_ = 0
    list2_ = []
    while intial_ < len_:
        list2_.append(fun_(list1_[intial_]))
        intial_ = intial_ + 1
    return list2_
def main():
    '''Main program start here'''
    data_ = input()
    data_ = data_.split(' ')
    list1_ = []
    for j in data_:
        list1_.append(int(j))
    print(apply_to_each(list1_, abs))

if __name__ == "__main__":
    main()
