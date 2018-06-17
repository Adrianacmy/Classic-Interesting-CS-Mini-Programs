'''

bubble sort 

'''

def bubble_sort(lst):
    '''
    :param lst: a list
    :return: sorted list
    '''
    # for i in range(len(lst)-1):
    #     for j in range(i + 1, len(lst)):
    #         if lst[i] > lst[j]:
    #             lst[i], lst[j] = lst[j], lst[i]
    # return lst


    is_sorted = False
    while not is_sorted:
        swap_count = 0
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swap_count += 1
        if swap_count == 0:
            is_sorted = True
    return lst



lst = [8, 3, 0, 500, -8, -9, 200]
print(bubble_sort(lst))

