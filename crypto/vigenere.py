
from helpers import alphabet_position, rotate_character


'''
vigenere cipher:
  Vigenere uses a word as the encryption key, rather than an integer.
'''

def get_rots(key):
    '''
    :param key: a string with only letters 
    :return: a generator
    '''
    i = 0
    while True:
        if i == len(key):
            i = 0

        yield key[i]
        i += 1


def encrypt(text, key):
    '''
    :param text: a string
    :param rot: a word with only letters
    :return: encrypted text with vegenere cipher
    '''
    encrypted_text = ''
    rot_gen = get_rots(key) #rot generator

    for achar in text:
        if achar.isalpha():
            rot = alphabet_position(next(rot_gen)) #generate a rot for each char
            encrypted_text += rotate_character(achar, rot)
        else:
            encrypted_text += achar

    return encrypted_text


#print(encrypt('ac7 !  54ya', 'abc'))
#print(encrypt('The crow flies at midnight!', 'boom'))

def main():

    from sys import argv, exit
    #print("This is what the user typed on the command line:", argv)

    if len(argv) >= 2:
        for achar in argv[1]:
            if not argv[1].isalpha():
                print('''usage: python vigenere.py keyword
Arguments:
 -keyword : The string to be used as a "key" to encrypt your message. Should
  only contain alphabetic characters-- no numbers or special characters.''')
                exit()
    else:
        print('''usage: python vigenere.py keyword
Arguments:
 -keyword : The string to be used as a "key" to encrypt your message. Should
 only contain alphabetic characters-- no numbers or special characters.''')
        exit()

    text = input('Type a message: \n')
    encrypted_text = encrypt(text, argv[1])

    print(encrypted_text)



if __name__ == '__main__':
    main()

