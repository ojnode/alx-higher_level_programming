#!/usr/bin/python3

def new_in_List(my_list, idx, element):
    l_len = len(my_list)
    if idx >= l_len or idx < 0:
        return (my_list)

    new_list = my_list[:]
    new_list[idx] = element
    return (new_list)
