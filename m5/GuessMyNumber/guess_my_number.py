''' Program starts here'''
print("Please think of the number between 0 and 100")
HIGH_ = 100
LOW_ = 0
AVG_ = 0
GUESS_ = 50
print("Is your secret number" + str(50))
print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low.")
print("Enter 'c' to indicate I guessed correctly.")
while 1:
    AVG_ = int((LOW_+HIGH_)/2)
    print("Is your secret number" + str(AVG_))
    NEW_ = input()
    if NEW_ == 'h':
        HIGH_ = AVG_
    elif NEW_ == 'l':
        LOW_ = AVG_
    elif NEW_ == 'c':
        print("Game over. Your secret number was:" + str(AVG_))
        break
    else:
        print("Sorry, I did not understand your input")
        break
