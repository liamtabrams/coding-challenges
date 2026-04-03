def split(index_list):
    mid = len(index_list)//2
    return index_list[:mid], index_list[mid:]

def check_is_in_left(target, sorted_list, left_list):
    if target > sorted_list[left_list[-1]]:
        return False
    else:
        return True

def recursive_function(target, sorted_list, index_list):
    if len(index_list) == 0:
        return -1
    elif len(index_list) == 1:
        if sorted_list[index_list[0]] != target:
            return -1
        else:
            return index_list[0]
    left_list, right_list = split(index_list)
    if check_is_in_left(target, sorted_list, left_list):
        return recursive_function(target, sorted_list, left_list)
    else:
        return recursive_function(target, sorted_list, right_list)


def binary_search(target, sorted_list):
    """
    This is an implementation of binary search to find the index of a given value in 
    a list. Note that the list needs to be sorted in order for binary search to work.
    If the value is not found in the list, return -1.
    """
    indices = [i for i in range(len(sorted_list))]
    return recursive_function(target, sorted_list, indices)



