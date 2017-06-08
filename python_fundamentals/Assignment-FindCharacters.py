'''
# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output
new_list = ['hello','world']
'''
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
newlist = []

def FindCharacters(char, word_list):
    for my_string in word_list:
        if (my_string.find(char)> -1):
            newlist.append(my_string)
    print newlist

FindCharacters(char, word_list)
