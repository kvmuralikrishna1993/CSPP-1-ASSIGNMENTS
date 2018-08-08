'''#Exercise : Odd Tuples
#Write a python function oddTuples(aTup) that
takes a some numbers in the tuple as input and
returns a tuple in which contains odd index values in the input tuple'''
def oddtuples_(tup_):
    '''aTup: a tuplereturns: tuple, every other element of aTup.'''
    len_ = len(tup_)
    newtup_ = ()
    intial_ = 0
    while intial_ < len_:
        newtup_ += (tup_[intial_],)
        intial_ += 2
    return newtup_
def main():
    '''Main program starts here'''
    data = input()
    data = data.split(',')
    tup_ = ()
    for j in range(len(data)):
        tup_ += (str(data[j]),)
    print(oddtuples_(tup_))
if __name__ == "__main__":
    main()
