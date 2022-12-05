#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    for i in (my_list):
        if not my_list:
            return none
        if my_list == []:
            return none
        if my_list:
            new_list = my_list[:]
        if idx < 0 and idx > len(my_list)-1:
            return(my_list)
        else:
            new_list[idx] = element
            return(new_list)
