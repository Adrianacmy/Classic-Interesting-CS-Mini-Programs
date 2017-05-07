def alphabet_position(achar):
    '''

    :param achar: a char 
    :return: a zero base ordinal of the char
    '''
    char_ord = ord(achar)

    if char_ord <= ord('z') and char_ord >= ord('a'):  # if a char is lowercase
        return ord(achar) - ord('a')
    elif char_ord <= ord('Z') and char_ord >= ord('A'):  # if a char is uppercase
        return ord(achar) - ord('A')
    else:
        return char_ord


def rotate_character(char, rot):
    '''
    :param char: a string of length 1
    :param rot: rot could be negative integer here, but during encryption, the user input has to be digit, since 
            I used isdigit for validation.
    :return: return the char after rotating rot 
    '''

    char_ord = alphabet_position(char)

    if ord(char) >= ord('a') and ord(char) <= ord('z'):
        encrypted_ord = (char_ord + rot) % 26 + ord('a')
    elif ord(char) >= ord('A') and ord(char) <= ord('Z'):
        encrypted_ord = (char_ord + rot) % 26 + ord('A')
    else:
        encrypted_ord = char_ord

    return chr(encrypted_ord)


