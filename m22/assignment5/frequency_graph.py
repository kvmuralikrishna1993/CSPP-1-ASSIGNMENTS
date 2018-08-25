'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    '''Frequency function'''
    list_ = []
    for i, j in dictionary.items():
        list_.append(i+' - '+ '#'*j)
    list_.sort()
    for i in list_:
        print(i)
def main():
    '''main function'''
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
