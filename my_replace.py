
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



start = 0
nw_str = ''
print(replace_one('banana', 'an', '', start, nw_str))
print(replace_all('banana', 'an', 'xy'))
print(replace_all('apple', 'pp', ''))


########################################################################################################################
'''
a much cleaner way to replace
'''

def get_next_target(s, old):
    '''
    :param s: a string 
    :param old: search string
    :return: search start and end index in the string
    '''
    start = s.find(old)
    end = start + len(old)
    return end, start


def my_replace(s, old, new):
    '''
    :param s: a string 
    :param old: a string
    :param new: a string
    :return: another string replaced old with new
    '''
    lst_s = []
    while s.find(old) != -1:  # if old is not in the string, end the loop and append the string to the list lst_s
        end, start = get_next_target(s, old)
        lst_s.append(s[:start])
        lst_s.append(new)
        s = s[end:]

    lst_s.append(s)

    return ''.join(lst_s)


s2 = 'Mississippi'
s1 = 'I love spom! Spom is my favorite food. Spom, spom, spom, yum!'
print(my_replace(s2, 'i', 'I'))
print(my_replace(s1, 'om', 'am'))
print(my_replace(s1, 'o', 'a'))