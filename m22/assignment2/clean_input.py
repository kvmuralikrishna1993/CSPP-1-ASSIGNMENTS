'''Write a function to clean up a given string by removing the
special characters and retain
alphabets in both upper and lower case and numbers.
'''
import re

def clean_string(string):
    '''clean the string'''
    return re.sub(r'[^a-zA-Z0-9]', r'', string)
def main():
    '''Main function'''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
