# Write a procedure, convert_seconds, which takes as input a non-negative 
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#

def convert_seconds(t):
   
    h = t // 3600
    m = t % 3600 // 60
    s = t % 3600 % 60
    return '%i hour%s, %i minute%s, %s second%s' % (h, 's' if h != 1 else '', 
                                                    m, 's' if m != 1 else '',
                                                    s, 's' if s != 1 else '')
print(convert_seconds(5689122))