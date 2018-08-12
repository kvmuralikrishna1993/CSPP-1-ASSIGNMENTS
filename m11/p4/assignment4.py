'''#Exercise: Assignment-4
#We are now ready to begin writing the code that interacts with the player.
We'll be implementing the playHand function.
This function allows the user to play out a single hand.
First, though, you'll need to implement the helper calculateHandlen function,
which can be done in under five lines of code.'''

def calculatehandlen(hand_):
    """
    Returns the length (number of letters) in the current hand.
    hand: dictionary (string int)
    returns: integer
    """
    count_ = 0
    for i in hand_.values():
        count_ = count_ + i
    return count_

def main():
    '''
    n: length of the dictionary
    '''
    num_ = input()
    adict_ = {}
    for i in range(int(num_)):
        data_ = input()
        list_ = data_.split()
        adict_[list_[0]] = int(list_[1])
    print(calculatehandlen(adict_))

if __name__ == "__main__":
    main()
