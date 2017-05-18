'''different ways to check palindrome'''

def is_palindrome(word):
    return word == word[::-1]

    
def is_palindrome1(word):
    for i in range(len(word)/2):
        if word[i] != word[-(i + 1)]:
            return False
    return True


def is_palindrome2(word):
    if word == '':
        return True
    else:
        if word[0] == word[-1]:
            return is_palindrome2(word[1:-1])
        else:
            return False