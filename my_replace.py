import string

'''
my replace
'''


def replace_one(aString, old, new, start, nw_str):

    idx = aString.find(old)

    if idx != -1:
        nw_str = aString[:idx] + new + aString[idx + len(old):]
    else:
        nw_str = aString

    return [nw_str, idx+start]


def replace_all(aString, old, new, start = 0):

    nw_str = ''

    while aString[start:]:
        nw_str, idx = replace_one(aString, old, new, start, nw_str)
        start = idx + len(old)
        aString = nw_str

    return nw_str


def replace_all_in_sentence(sentence, old, new, start = 0):
    nw_str = ''

    for word in sentence:
        nw_str += replace_all(word, old, new)

    return nw_str

#start = 0
#nw_str = ''
#print(replace_one('banana', 'an', '', start, nw_str))
print(replace_all('banana', 'an', 'xy'))
print(replace_all('apple', 'pp', ''))
s = 'I love spom! Spom is my favorite food. Spom, spom, spom, yum!'
#print(replace_all_in_sentence(s,'o', 'a'))
#print(replace_all_in_sentence(s,'om', 'am'))
print('abc'.replace('a', 'd'))
