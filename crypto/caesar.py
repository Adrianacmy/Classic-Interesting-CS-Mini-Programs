
from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    '''
    :param text: a string
    :param rot: an integer
    :return: an encrypted string
    '''
    encrypted = ''
    for char in text:
        encrypted += rotate_character(char, rot)

    return encrypted


def main():
    from sys import argv, exit

    if len(argv) >= 2:
        if not argv[1].isdigit():
            print('''usage: python caesar.py n
Arguments:
-n : any digits. ''')
            exit()
    else:
        print('''usage: python caesar.py n
Arguments:
-n : any integer. ''')
        exit()


    text = input('Type a message: \n')
    encrypted_text = encrypt(text, int(argv[1]))

    print(encrypted_text)



if __name__ == '__main__':
    main()

#print(alphabet_position('a'))
#print(alphabet_position('A'))
#print(alphabet_position('!'))

#print(rotate_character('A', 26))
#print(rotate_character('!', 56))
#fprint(encrypt('abc!@--  50!', -12))

