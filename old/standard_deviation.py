def cacu_standard_deviation(lst):
    
    mean = sum(lst)/len(lst)
    sum_m = 0
    for element in lst:
        sum_m += (mean - element)**2
    return (sum_m/len(lst))**0.5

lst = [4, 11, 6 , 7]
print(cacu_standard_deviation(lst))