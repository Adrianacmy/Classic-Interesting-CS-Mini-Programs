# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def shift_n_letters(letter, n):
   ord_l = ord(letter)
   return chr((ord_l + n - 97) % 26 + 97)

    
def rotate(str, n):
    new_str = ''
    for s in str:
        if not s.isalpha():
            new_str += ' '
        else:
            new_str += shift_n_letters(s, n)
    return new_str

print(rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17))
