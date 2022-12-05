#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return none
    if my_list == []:
        return none
    else:
        for i in range (len(my_list)-1, -1, -1):
            print('{:d}'.format(my_list[i]))
