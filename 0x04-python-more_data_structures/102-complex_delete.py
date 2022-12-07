#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    myDel = []
    for i, j in a_dictionary.items():
        if j == value:
            myDel.append(i)
    for i in myDel:
        a_dictionary.pop(i)
    return a_dictionary
