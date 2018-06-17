
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on Sun May  15 

@author: Adrianacmy

Create a function reverse that takes in a dictionary and reverses it, such that 
all of the values become keys and all of the keys become values. Be careful: we 
do not wish to lose any information. Consider what to do if the original 
dictionary has lists of values for a particular key, or has duplicate values 
for some keys.

'''

# def format_dic_value(dict):
#     '''format the single elements value list if it is necessary'''

#     nw_dict = {}
#     for k, v in dict.items():
#         if len(v) == 1 and type(v) == list:
#             nw_dict[k] = ''.join(v)
#         else:
#             nw_dict[k] = v

#     return nw_dict


def convert_to_simple_list(lst, nw_list=[]):
    '''
    Convert a muti-dimentinal list to one dimention list.
    lst: any list 
    nw_list: one dimentiona list, could start as empty 
    return: a one dimention list
    '''
    for a in lst:
        if type(a) == list:
            convert_to_simple_list(a)
        else:
            nw_list.append(a)
    return nw_list

# lst = ['a', 'b', 'c', [1,2,3], 'abc']
# print(convert_to_simple_list(lst))


def add_dic_val(dic, k, v):
    '''
    add elements or values to a dictionary. 
    dic: an empty dictionary 
    k: a key  
    v: a value 
    '''
    dic[k] = dic.get(k, [])
    if not v in dic[k]:
        dic[k].append(v)


def reverse_dict(d):
    '''reverse keys and values in a dictionary'''
    
    r = {}  #reversed dictionary

    for k, v in d.items():
        nw_lst = []
        if type(v) == list:
            value_list = convert_to_simple_list(v, nw_lst)
            # if value_list:
            for val in value_list:
                add_dic_val(r, val, k) 
        else:
            add_dic_val(r, v, k)
           
    return r


def main():
    d = {1: 'a', 4: ['abc', 'egf'], 5: '',(1, 6): 'abc', 2:[1, 2, 3, [1, 2]], 8: ['', 2]}
    print(reverse_dict(d))


if __name__ == "__main__":
    main()



