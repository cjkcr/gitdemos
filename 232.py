
# from bs4 import BeautifulSoup
# import requests
#
# baibu=requests.get('https://www.baidu.com').content
#
# soup=BeautifulSoup(baibu,'html.parser')
#
# links=soup.findAll('a')
#
# for link in links:
#     print(link.string)
#
# input()

# x = 'there are %d types of  people.'%10
# binary = 'binary'
# do_not = 'don\'t'
# y = 'those who inow %s and those who %s.'%(binary,do_not)
#
# print(x)
# print(y)
# print('i said: %r.'%x)
# print("i also said: '%s'." %y)
#
# hilarious = False
# joke_evaluation ='isn\'t that joke so funny?!%r'
#
# print(joke_evaluation %hilarious)
#
# w = 'this is the left side of...'
# e = 'a string with a right side.'
# print(w+e)

# def printtwo(*args):
#     arg1,arg2=args
#     print('arg1:%r,arg2:%r'%(arg1,arg2))
# printtwo('zed','shaw')

def break_words(stuff):
    '''this function will break up words for us.'''
    words = stuff.split('')
    return words
def sort_words(words):
    '''sorts the words.'''
    return sorted(words)
def print_first_word(words):
    '''print the first word after popping it off.'''
    word = words.pop(0)
    print(word)

def print_last_word(words):
    '''prints the last word after popping it off.'''
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    '''takes in a full sentence and returns the sorted words.'''
    word =break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    '''print the first and last words of the sentence.'''
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    '''sorts the words then prints the first and laat one.'''
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
