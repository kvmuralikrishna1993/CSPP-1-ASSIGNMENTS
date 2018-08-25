'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re
def tokenize(string):
    '''token function'''
    dictionary = {}
    for i in string:
        if i not in dictionary:
            dictionary[i] = string.count(i)
    return dictionary
def main():
    '''Main function'''
    num = int(input())
    intial = 0
    string = []
    while intial < num:
        string.extend(input().split())
        intial += 1
    newstring = []
    for i in string:
        newstring.append(re.sub(r'[^a-zA-Z0-9]', r'', i))
    print(tokenize(newstring))
if __name__ == '__main__':
    main()
