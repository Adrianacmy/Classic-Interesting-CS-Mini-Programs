
def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    # TODO your code here

    initials = ''

    for i in fullname.split():
        initials += i[0].capitalize()

    return initials


def main():

    fullname = input('What is your name?')
    ozzie_inits = get_initials(fullname)
    print('The initials of ', fullname, 'are', ozzie_inits)

if __name__ == '__main__':
    main()


