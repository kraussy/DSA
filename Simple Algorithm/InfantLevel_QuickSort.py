def quick_sort(array):
    if len(array) <= 1:
        return array

    

    less_list = []
    pivot_list = []
    more_list = []
    pivot_value = array[0]

    for value in array:
        if value < pivot_value:
            less_list.append(value)
        
        elif value > pivot_value:
            more_list.append(value)
        
        else:
            pivot_list.append(value)
    
    left = quick_sort(less_list)
    right = quick_sort(more_list)
    return left + pivot_list + right


    
