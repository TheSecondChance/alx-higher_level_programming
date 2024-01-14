#!/usr/bin/python3
"""peak in a list unsorted integers"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of integers to find peak
    """
    lenOfListIntegeres = len(list_of_integers)
    yemehal = lenOfListIntegeres
    keme = lenOfListIntegeres // 2

    if lenOfListIntegeres == 0:
        return None

    while True:
        yemehal = yemehal // 2
        if (keme < lenOfListIntegeres - 1 and
                list_of_integers[keme] < list_of_integers[keme + 1]):
            if yemehal // 2 == 0:
                yemehal = 2
            keme = keme + yemehal // 2
        elif yemehal > 0 and list_of_integers[keme] < list_of_integers[keme - 1]:
            if yemehal // 2 == 0:
                yemehal = 2
            keme = keme - yemehal // 2
        else:
            return list_of_integers[keme]
