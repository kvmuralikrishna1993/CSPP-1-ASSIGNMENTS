'''Exercise: Assignment-1
First, implement the function isWordGuessed that
takes in two parameters -
a string, secret_word, and a list of letters,
letters_guessed. This function
returns a boolean - True if secret_word has been guessed
(ie, all the letters of
secret_word are in letters_guessed) and False otherwise.
'''
def is_word_guessed(secret_word, letters_guessed):
    '''secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean,True if all the letters of
    secret_word are in letters_guessed;False otherwise'''
    len1_ = len(secret_word)
    len2_ = len(letters_guessed)
    word_ = ''
    for i in range(len1_,):
        flag = 1
        for j in range(len2_):
            if secret_word[i] == letters_guessed[j]:
                word_ = word_ + letters_guessed[j]
                flag = 0
                break
        if flag == 1:
            word_ = word_ + '_'
    return word_ == secret_word

def main():
    '''Main function for the program'''
    user_input = input()
    if user_input:
        data_ = user_input.split(' ')
        secret_word = data_[0]
    else:
        data_ = []
        secret_word = ""
    list1_ = []
    for j in range(1, len(data_)):
        list1_.append(data_[j][0])
    print(is_word_guessed(secret_word, list1_))

if __name__ == "__main__":
    main()
