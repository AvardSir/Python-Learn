def check_set_in():
    num_set = {1, 2, 3, 4, 5}

    print(3 in num_set)
def more_check_set_in():
    letters = {"a", "b", "c", "d"}
    if "e" not in letters:
      print(1)
    else: 
      print(2)

def add_remove_in_sets():

    nums = {1, 2, 1, 3, 1, 4, 5, 6}
    print(nums)
    nums.add(-7)
    nums.remove(3)
    print(nums)
    
def operation_on_sets():

    first = {1, 2, 3, 4, 5, 6}
    second = {4, 5, 6, 7, 8, 9}
    '''
    The union operator | combines two sets to form a new one containing items in either. 

    The intersection operator & gets items only in both. 

    The difference operator - gets items in the first set but not in the second. 

    The symmetric difference operator ^ gets items in either set, but not both.'''
    print(first | second)
    print(first & second)
    print(first - second)
    print(second - first)
    print(first ^ second)


def check_operation_on_sets():
    a = {1, 2, 3}
    b = {0, 3, 4, 5}
    print(a & b)