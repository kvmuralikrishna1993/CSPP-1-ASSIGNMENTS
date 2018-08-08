'''#Exercise : Function and Objects Exercise-2
#Implement a function that converts the given testList = [1, -4, 8, -9] into [2, -3, 9, -8]'''
def apply_to_each(list1_, incr_):
    '''fucntion starts here'''
    len_ = len(list1_)
    intial_ = 0
    list2_ = []
    while intial_ < len_:
        list2_.append(incr_(list1_[intial_]))
        intial_ = intial_ + 1
    return list2_
def inc_(num_):
    '''increment fucntion starts here'''
    num_ = num_ + 1
    return num_
def main():
    '''Main fucntion starts here'''
    data_ = input()
    data_ = data_.split()
    list1_ = []
    for j in data_:
        list1_.append(int(j))
    print(apply_to_each(list1_, inc_))

if __name__ == "__main__":
    main()
