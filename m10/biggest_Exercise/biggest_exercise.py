'''#Exercise : Biggest Exercise
#Write a procedure, called biggest, which returns
the key corresponding to the entry with
the largest number of values associated with it.
If there is more than one such entry,
return any one of the matching keys.'''
def biggest_(adict_):
    '''aDict: A dictionary, where all the values are lists.
    returns: The key with the largest number of values associated with it'''
    key_ = list(adict_.keys())
    val_ = list(adict_.values())
    varlen_ = []
    for i in val_:
        varlen_.append(len(i))
    index_ = varlen_.index(max(varlen_))
    return key_[index_]

def main():
    '''Main program starts here'''
    num_ = input()
    adict_ = {}
    for i in range(int(num_)):
        set_ = input()
        mset_ = set_.split()
        if mset_[0][0] not in adict_:
            adict_[mset_[0][0]] = [mset_[1]]
        else:
            adict_[mset_[0][0]].append(mset_[1])
    print(biggest_(adict_))
if __name__ == "__main__":
    main()
