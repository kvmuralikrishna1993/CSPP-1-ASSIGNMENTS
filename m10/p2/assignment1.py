'''Exercise : Assignment-1
implement the function get_available_letters that
takes in one parameter -
a list of letters, letters_guessed.
This function returns a string
that is comprised of lowercase English letters
all lowercase English letters
that are not in letters_guessed'''
def get_available_letters(letters_guessed):
    ''':param letters_guessed: list, what letters have been guessed
    so farreturns: string, comprised of letters that represents
    what letters have not yet been guessed.'''
    list_ = []
    str_ = ''
    for i in range(97, 123):
        if chr(i) not in letters_guessed:
            list_.append(chr(i))
    return str_.join(list_)

def main():
    '''Main function for the given program'''
    user_input = input()
    user_input = user_input.split(' ')
    data_ = []
    for char_ in user_input:
        data_.append(char_[0])
    print(get_available_letters(data_))
if __name__ == "__main__":
    main()
