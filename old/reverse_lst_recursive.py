

def reverse_lst(lst):
    '''reverse a list use recursion'''
    
   return [lst[-1]] + reverse_lst(lst[:-1]) if lst else []
   
lst = []
lst2 = [1,2,3,4,5]

print(reverse_lst(lst2))

