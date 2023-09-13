#!/usr/bin/python3
def weight_average(my_list=[]):
    total = 0
    denom = 0
    if my_list == []:
        return 0
    for fir in my_list:
        total += fir[0] * fir[1]
        denom += fir[1]
    return total/denom
