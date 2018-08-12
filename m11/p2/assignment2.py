'''#Exercise: Assignment-2
#Implement the updateHand function.
Make sure this function has no side effects:
i.e., it must not mutate the hand passed in.
Before pasting your function definition here,
be sureyou've passed the appropriate tests in test_ps4a.py.'''
def updatehand_(hand_, word_):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.
    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.
    Has no side effects: does not modify hand.
    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)"""
    set_ = {}
    for i in hand_:
        if i in word_:
            set_[i] = hand_[i] - word_.count(i)
        else:
            set_[i] = hand_[i]
    return set_
def main():
    '''Main program starts here'''
    num_ = input()
    adict_ = {}
    for i in range(int(num_)):
        data_ = input()
        len_ = data_.split()
        adict_[len_[0]] = int(len_[1])
    data1_ = input()
    print(updatehand_(adict_, data1_))
if __name__ == "__main__":
    main()
