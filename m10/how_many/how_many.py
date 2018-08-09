''''#Exercise : how many
# write a procedure, called how_many,
which returns the sum of the number of values associated
with a dictionary.'''
def how_many(adict_):
    '''aDict: A dictionary, where all the values are lists.
    returns: int, how many values are in the dictionary.'''
    val_ = list(adict_.values())
    varlen_ = []
    sum_ = 0
    for i in val_:
        varlen_.append(len(i))
    for i in varlen_:
        sum_ = sum_ + i
    return sum_

def main():
    '''Main function starts here'''
    num_ = input()
    adict_ = {}
    for i in range(int(num_)):
        set_ = input()
        lr_ = set_.split()
        if lr_[0][0] not in adict_:
            adict_[lr_[0][0]] = [lr_[1]]
        else:
            adict_[lr_[0][0]].append(lr_[1])
    print(how_many(adict_))
if __name__ == "__main__":
    main()
