# Deep Count 

# The built-in len operator outputs the number of top-level elements in a List,
# but not the total number of elements. For this question, your goal is to count
# the total number of elements in a list, including all of the inner lists.

# Define a procedure, deep_count, that takes as input a list, and outputs the
# total number of elements in the list, including all elements in lists that it
# contains.



def is_list(p):
    return isinstance(p, list)


def deep_count(p):
    sum = 0
    for i in p:
        sum += 1
        if is_list(i):
            sum += deep_count(i)
        
    return sum 

print(deep_count([1, 2, 3]))
#>>> 3

# The empty list still counts as an element of the outer list
print(deep_count([1, [], 3])) 
#>>> 3 

print(deep_count([1, [1, 2, [3, 4]]]))

 