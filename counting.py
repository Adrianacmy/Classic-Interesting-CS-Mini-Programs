'''

Write a program that calculates the number of times each character occurs in a 
string and prints these stats to the console. You could get the string as input
from the user, but for the sake of simplicity, you may also hard-code the 
string into your program as the value of a variable.
'''

def create_count_dict(aString):
    
    dict = {}
    for achar in aString:
        dict[achar] = dict.get(achar, 0)
        dict[achar] += 1

    return dict


def print_dict(dict):
    dict = create_count_dict(aString)
    for k, v in dict.items():
        print(k, ':', v)

    return ' '


def main():
    aString = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
    Nunc ! 56 '''

    print(print_dict(create_count_dict(aString))


if __name__ == '__main__':
    main()


