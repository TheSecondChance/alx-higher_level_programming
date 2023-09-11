#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == 0:
        return None
    max = my_list[0]
    else:
        for in range(len(my_list)):
            if my_list[i] > max:
                max = my_list[i]
        return max
