'''
takes a text document as input
counts the frequency of each unique word in the document
test
'''

def word_frequency_1(file):
    text = file.read()
    text_list = text.split()
    word_dict = dict()
    for word in text_list:
        exclude = [',','.',';',':','"',"'s",'?',')','(','[',']']
        word = word.lower()
        for i in exclude:
            if i in word:
                word = word.replace(i, '')
        if word == '' or word.isdigit():
            continue
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    #print(word_dict)
    print(len(word_dict))

if __name__ == '__main__':
    file = open('textfile.txt')
    word_frequency_1(file)
