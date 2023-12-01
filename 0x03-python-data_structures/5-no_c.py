#!/usr/bin/python3
def no_c(my_string):
    m = list(my_string)
    for char in m:
        if char == 'c' or char == 'C':
            m.remove(char)
    return("".join(m))
