def average(array):
    # your code goes here
    num_set = set(array)
    sum_set = 0
    set_size = len(num_set)
    for i in range(set_size):
        sum_set+= int(num_set.pop())

    return(sum_set/set_size)
