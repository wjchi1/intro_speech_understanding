

def cancellation(list, stop_word):
    output_list = []
    for elements in list:
        if elements == stop_word:
            break
        else:
            output_list.append(elements)
    return output_list
    '''
    Copy elements one by one from input_list into output_list. 
    If one of the elements is equal to the stop_word, then stop the function,
    and return what you have so far.
    '''
    

def copy_all_but_skip_word(input_list, skip_word):
    output_list = []
    for elements in input_list:
        if elements == skip_word:
            continue
        else:
            output_list.append(elements)
    return output_list
    '''
    This function should copy elements one by one from input_list into output_list.
    If one of the elements is equal to the skip_word, then you should skip that element,
    but keep checking all of the other elements.
    '''
    pass

def my_average(input_list):
    if len(input_list) == 0:
        print("input_list is empty")
    else:
        sum = 0 
        for elements in input_list:
            sum += elements
        average = sum/len(input_list)
        return average
    '''
    You may assume that `input_list` is a non-empty list, in which every element is a number.  
    Calculate the average value, and return it. 
    '''
    pass

