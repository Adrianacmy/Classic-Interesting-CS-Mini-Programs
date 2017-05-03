'''Write a function that implements a substitution cipher. In a substitution cipher one letter is substituted for
another to garble the message. For example A -> Q, B -> T, C -> G etc. your function should take two parameters,
the message you want to encrypt, and a string that represents the mapping of the 26 letters in the alphabet. Your
function should return a string that is the encrypted version of the message.

'''

# Move each letter in string n to it's right or left
# boundaries:( A: 65   Z: 90  a: 97  z:122)

import string


def move_n(s, n):
    ''' s : a string with only letters
        n :  any integer
        return a new string with after n move
    '''
    s_ord = ord(s)

    # only move around upper case or lowercase
    if s_ord <= ord('z') and s_ord >= ord('a'):
        nw_ord = s_ord + n - ord('a')
        nw_char = chr(nw_ord % 26 + ord('a'))
    else:
        nw_ord = s_ord + n - ord('A')
        nw_char = chr(nw_ord % 26 + ord('A'))

    return nw_char


def caesar_cipher_n(astring, n=13):
    '''return a string after n move, if n is not supplied, default is 13'''

    letters = string.ascii_letters
    nw_str = ''

    for achar in astring:
        if achar in letters:
            nw_str += move_n(achar, n)
        else:
            nw_str += achar

    return nw_str


print(caesar_cipher_n('abcde', 0))
print(caesar_cipher_n('nopqr', 1))
print(caesar_cipher_n(caesar_cipher_n('since rot thirteen is symmetric you should see this message')))
print(caesar_cipher_n('This function only encrypt letters, the rest remain the same, SUCH AS @_@, :),2333, 6666... ', 2))
