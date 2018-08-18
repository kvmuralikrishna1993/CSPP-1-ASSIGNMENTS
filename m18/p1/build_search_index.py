'''
    Tiny Search Engine - Part 1 - Build a search index

    In this programming assingment you are given with some text documents as input.
    Complete the program below to build a search index. Don't worry, it is explained below.
    A search index is a python dictionary.
    The keys of this dictionary are words contained in ALL the input text documents.
    The values are a list of documents such that the key/word appears in each document atleast once.
    The document in the list is represented as a tuple.
    The tuple has 2 items. The first item is the document ID.
    Document ID is represented by the list index.
    For example: the document ID of the third document in the list is 2
    The second item of the tuple is the frequency of the word occuring in the document.

    Here is the sample format of the dictionary.
    {
        word1: [(doc_id, frequency),(doc_id, frequency),...],
        word2: [(doc_id, frequency),(doc_id, frequency),...],
        .
        .
    }
'''
import re
# helper function to load the stop words from a file
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords


def word_list(text):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''
    text = text.lower()
    list_ = []
    list_ = text.split()
    list1_ = [re.sub(r'[?|$|.|!]', r'', i) for i in list_]
    list2_ = [re.sub(r'[^a-z ]', r'', i) for i in list1_]
    commonwords = load_stopwords("stopwords.txt")
    final = [word for word in list2_ if (word not in commonwords and len(word) > 0)]
    return final
def build_search_index(docs):
    '''
        Process the docs step by step as given below
    '''

    # initialize a search index (an empty dictionary)
    dictionary = {}
    doc_id = []
    clean_doc = []
    # iterate through all the docs
    for i, item in enumerate(docs):
        doc_id.append([i, item])
    for i, item in doc_id:
        clean_doc.append([i, word_list(item)])
    for i, item in enumerate(clean_doc):
        for j in item[1]:
            if j not in dictionary:
                dictionary[j] = [(i, item[1].count(j))]
            else:
                dictionary[j].append((i, item[1].count(j)))
    for key_, value_ in dictionary.items():
        dictionary[key_] = list(set(value_))
    print_search_index(dictionary)

    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop

        # clean up doc and tokenize to words list

        # add or update the words of the doc to the search index

    # return search index
# helper function to print the search index
# use this to verify how the search index looks
def print_search_index(index):
    '''
        print the search index
    '''
    keys_ = []
    try:
        keys_ = (index.keys())
    except AttributeError:
        exception_ = []
    keys_ = sorted(keys_)
    for key in keys_:
        print(key, " - ", sorted(index[key]))

# main function that loads the docs from files
def main():
    '''
        main function
    '''
    # empty document list
    documents = []
    # iterate for n times
    lines = int(input())
    # iterate through N times and add documents to the list
    for i in range(lines):
        documents.append(input())
        i += 1
    # call print to display the search index
    #build_search_index(documents)
    print_search_index(build_search_index(documents))

if __name__ == '__main__':
    main()
