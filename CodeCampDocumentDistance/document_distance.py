'''Progrqm starts here'''
import math
import re
def wordlist(input_):
    '''Creating Wordlist '''
    inputlist = []
    input1_ = input_.lower()
    inputlist = input1_.split(' ')
    input2_ = [re.sub(r'[?|$|.|!]', r'', i) for i in inputlist]
    input3_ = [re.sub(r'[^a-z ]', r'', i) for i in input2_]
    commonwords = load_stopwords("stopwords.txt")
    return [word for word in input3_ if word not in commonwords and len(word) > 0]

def calculate(wordset_):
    '''Frequency of words'''
    numerator = sum([i[0]*i[1] for i in wordset_.values()])
    denominator = (math.sqrt(sum([i[0]**2 for i in wordset_.values()])))* \
                    (math.sqrt(sum([i[1]**2 for i in wordset_.values()])))
    if denominator == 0:
        return 0.0
    return numerator/denominator

def freq(words1, words2):
    '''Frequency fucntion'''
    dictionary = {}
    for i in words1:
        if i not in dictionary:
            dictionary[i] = [words1.count(i), words2.count(i)]
    for i in words2:
        if i not in dictionary:
            dictionary[i] = [0, words2.count(i)]
    return dictionary

def similarity(dict1, dict2):
    '''
    Compute the document distance as given in the PDF
    '''
    common_dic = {}
    dict_1 = wordlist(dict1)
    dict_2 = wordlist(dict2)
    common_dic = freq(dict_1, dict_2)
    magnitude = calculate(common_dic)
    return magnitude

def load_stopwords(file_name):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(file_name, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()
    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
