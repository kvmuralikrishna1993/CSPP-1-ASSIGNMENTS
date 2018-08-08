'''#Exercise : Function and Objects Exercise-3
#Implement a function that converts the given
testList = [1, -4, 8, -9] into [1, 16, 64, 81]'''
def apply_to_each(list1_, sqa_):
    '''Fucntion starts here'''
    len_ = len(list1_)
    intial_ = 0
    list2_ = []
    while intial_ < len_:
        list2_.append(sqa_(list1_[intial_]))
        intial_ = intial_ + 1
    return list2_
def square_(num_):
    '''Square function'''
    return num_*num_
def main():
    '''Main function here'''
    data_ = input()
    data_ = data_.split()
    list1_ = []
    for j in data_:
        list1_.append(int(j))
    print(apply_to_each(list1_, square_))

if __name__ == "__main__":
    main()
