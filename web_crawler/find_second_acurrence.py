'''
Find the second accurrence of substring in another string. 

'''


def find_second_sub(sub, aString):
    '''
    :param sub: a string 
    :param aString: another string 
    :return: index of the second accurrence of sub in aString
    '''

    first_sub = aString.find(sub)

    return aString.find(sub, first_sub + 1)


print(find_second_sub('zip', 'zipfilezip'))